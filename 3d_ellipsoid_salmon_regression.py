import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import f
from sklearn.linear_model import LinearRegression

# ============================================
# 1. SIMULATE SALMON FARM DATA
# ============================================

np.random.seed(42)
n = 100  # number of pens

# Predictors: Feed (kg/day) and Temperature (°C)
Feed = np.random.normal(2.5, 0.6, n)
Temp = np.random.normal(12, 2, n)

# True coefficients (in real life, we don't know these!)
beta_0_true = -3.0   # intercept (kg)
beta_1_true = 1.8    # feed effect (kg per kg feed)
beta_2_true = 0.25   # temperature effect (kg per °C)

# Generate outcomes with some noise
sigma = 0.5  # standard deviation of the error
Y = beta_0_true + beta_1_true * Feed + beta_2_true * Temp + np.random.normal(0, sigma, n)

# Create DataFrame
df = pd.DataFrame({
    'Feed': Feed,
    'Temp': Temp,
    'Weight': Y
})

print("=== Salmon Farm Data ===")
print(df.head())
print(f"\nNumber of pens: {n}")
print(f"Mean Weight: {Y.mean():.2f} kg")
print(f"Mean Feed: {Feed.mean():.2f} kg/day")
print(f"Mean Temp: {Temp.mean():.2f} °C\n")

# ============================================
# 2. FIT THE MULTIPLE REGRESSION MODEL
# ============================================

# Design matrix: add intercept column
X = np.column_stack([np.ones(n), Feed, Temp])
p = X.shape[1]  # number of predictors including intercept

# OLS solution: beta_hat = (X'X)^(-1) X'Y
XTX = X.T @ X
XTX_inv = np.linalg.inv(XTX)
beta_hat = XTX_inv @ X.T @ Y

# Residuals and sigma^2
Y_hat = X @ beta_hat
residuals = Y - Y_hat
sigma_hat_sq = np.sum(residuals**2) / (n - p)

# Covariance matrix of coefficients
cov_beta = sigma_hat_sq * XTX_inv

# Standard errors
se_beta = np.sqrt(np.diag(cov_beta))

print("=== Regression Results ===")
print(f"Intercept: {beta_hat[0]:.4f} (se: {se_beta[0]:.4f})")
print(f"Feed:      {beta_hat[1]:.4f} (se: {se_beta[1]:.4f})")
print(f"Temp:      {beta_hat[2]:.4f} (se: {se_beta[2]:.4f})")
print(f"R²:        {1 - np.sum(residuals**2)/np.sum((Y - Y.mean())**2):.4f}")
print(f"Sigma:     {np.sqrt(sigma_hat_sq):.4f}\n")

# ============================================
# 3. GENERATE THE 2D CONFIDENCE ELLIPSE
# ============================================

def get_confidence_ellipse(beta_hat, cov_beta, alpha=0.05, n_points=100):
    """
    Generate points on the 2D confidence ellipse for Feed and Temp coefficients.
    
    Returns:
        ellipse_points: numpy array of shape (n_points, 2)
        f_crit: F-distribution critical value
        radius: Ellipse radius
    """
    # Number of predictors (excluding intercept)
    p_pred = len(beta_hat) - 1  # 2 predictors: Feed and Temp
    n = len(Y)
    
    # F-distribution critical value
    f_crit = f.ppf(1 - alpha, p_pred, n - p_pred - 1)
    
    # Radius of the ellipsoid
    radius = np.sqrt(p_pred * f_crit * sigma_hat_sq)
    
    # Covariance matrix for predictors only (exclude intercept)
    cov_pred = cov_beta[1:, 1:]  # 2x2 matrix
    
    # Eigen-decomposition of the covariance matrix
    eigvals, eigvecs = np.linalg.eigh(cov_pred)
    
    # Scale eigenvectors by sqrt of eigenvalues and radius
    D = np.diag(np.sqrt(eigvals))
    A = eigvecs @ D * radius  # 2x2 transformation matrix
    
    # Generate points on a unit circle (2D, not 3D!)
    theta = np.linspace(0, 2 * np.pi, n_points)
    
    ellipse_points = []
    for t in theta:
        # Unit circle point (2D)
        unit_circle = np.array([np.cos(t), np.sin(t)])
        # Transform to ellipse and center at beta_hat
        ellipse_point = A @ unit_circle + beta_hat[1:]
        ellipse_points.append(ellipse_point)
    
    return np.array(ellipse_points), f_crit, radius

# Generate ellipse points
alpha = 0.05  # 95% confidence
ellipse_points, f_crit, radius = get_confidence_ellipse(beta_hat, cov_beta, alpha)

# Extract coordinates
feed_ellipse = ellipse_points[:, 0]
temp_ellipse = ellipse_points[:, 1]

# ============================================
# 4. INTERACTIVE 2D VISUALIZATION WITH PLOTLY
# ============================================

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'scatter'}, {'type': 'scatter'}]],
    subplot_titles=('95% Confidence Ellipse', 'Zoomed View with Marginal CIs')
)

# --- Ellipse ---
fig.add_trace(
    go.Scatter(
        x=feed_ellipse,
        y=temp_ellipse,
        mode='lines',
        line=dict(color='blue', width=2),
        fill='toself',
        fillcolor='rgba(31, 119, 180, 0.2)',
        name='95% Confidence Ellipse'
    ),
    row=1, col=1
)

# Estimated coefficients
fig.add_trace(
    go.Scatter(
        x=[beta_hat[1]],
        y=[beta_hat[2]],
        mode='markers',
        marker=dict(
            size=12,
            color='red',
            symbol='x',
            line=dict(width=3)
        ),
        name='Estimated Coefficients'
    ),
    row=1, col=1
)

# True coefficients (for comparison - only known in simulation!)
fig.add_trace(
    go.Scatter(
        x=[beta_1_true],
        y=[beta_2_true],
        mode='markers',
        marker=dict(
            size=12,
            color='green',
            symbol='star',
            line=dict(width=2)
        ),
        name='True Coefficients'
    ),
    row=1, col=1
)

# --- Zoomed view with marginal CIs ---
# Same ellipse
fig.add_trace(
    go.Scatter(
        x=feed_ellipse,
        y=temp_ellipse,
        mode='lines',
        line=dict(color='blue', width=2),
        fill='toself',
        fillcolor='rgba(31, 119, 180, 0.15)',
        name='95% Ellipse'
    ),
    row=1, col=2
)

# Estimated coefficients
fig.add_trace(
    go.Scatter(
        x=[beta_hat[1]],
        y=[beta_hat[2]],
        mode='markers',
        marker=dict(size=12, color='red', symbol='x'),
        name='Estimate'
    ),
    row=1, col=2
)

# Marginal confidence intervals (vertical and horizontal lines)
t_crit = 1.96  # approximate for large n
ci_feed_lower = beta_hat[1] - t_crit * se_beta[1]
ci_feed_upper = beta_hat[1] + t_crit * se_beta[1]
ci_temp_lower = beta_hat[2] - t_crit * se_beta[2]
ci_temp_upper = beta_hat[2] + t_crit * se_beta[2]

# Horizontal lines (Feed CI)
fig.add_hline(
    y=ci_temp_upper, line_dash="dash", line_color="orange",
    annotation_text="Temp CI upper", row=1, col=2
)
fig.add_hline(
    y=ci_temp_lower, line_dash="dash", line_color="orange",
    annotation_text="Temp CI lower", row=1, col=2
)

# Vertical lines (Temp CI)
fig.add_vline(
    x=ci_feed_upper, line_dash="dash", line_color="orange",
    annotation_text="Feed CI upper", row=1, col=2
)
fig.add_vline(
    x=ci_feed_lower, line_dash="dash", line_color="orange",
    annotation_text="Feed CI lower", row=1, col=2
)

# Update layout
fig.update_layout(
    title=dict(
        text=f'95% Confidence Ellipse for Salmon Regression Coefficients<br>'
             f'F-critical = {f_crit:.3f}, Radius = {radius:.3f}',
        font=dict(size=16)
    ),
    width=1200,
    height=600,
    showlegend=True
)

fig.update_xaxes(title_text='Feed Coefficient (β₁)', row=1, col=1)
fig.update_yaxes(title_text='Temperature Coefficient (β₂)', row=1, col=1)
fig.update_xaxes(title_text='Feed Coefficient (β₁)', row=1, col=2)
fig.update_yaxes(title_text='Temperature Coefficient (β₂)', row=1, col=2)

# Show the plot
fig.show()

# ============================================
# 5. MARGINAL CONFIDENCE INTERVALS
# ============================================

print("=== 95% Marginal Confidence Intervals ===")
for i, name in enumerate(['Intercept', 'Feed', 'Temp']):
    t_crit = 1.96  # approximate for large n
    ci_lower = beta_hat[i] - t_crit * se_beta[i]
    ci_upper = beta_hat[i] + t_crit * se_beta[i]
    print(f"{name:12s}: [{ci_lower:.4f}, {ci_upper:.4f}]")

print("\n=== Interpretation ===")
print(f"We are 95% confident that:")
print(f"  - For every 1 kg increase in feed, weight increases between {beta_hat[1]-t_crit*se_beta[1]:.3f} and {beta_hat[1]+t_crit*se_beta[1]:.3f} kg.")
print(f"  - For every 1°C increase in temperature, weight increases between {beta_hat[2]-t_crit*se_beta[2]:.3f} and {beta_hat[2]+t_crit*se_beta[2]:.3f} kg.")

# ============================================
# 6. CHECK IF A SPECIFIC POINT IS INSIDE
# ============================================

def is_inside_ellipse(beta_point, beta_hat, cov_beta, alpha=0.05):
    """
    Check if a given point is inside the confidence ellipse.
    """
    p_pred = len(beta_point)
    n = len(Y)
    f_crit = f.ppf(1 - alpha, p_pred, n - p_pred - 1)
    
    diff = beta_point - beta_hat[1:]
    cov_pred = cov_beta[1:, 1:]
    mahalanobis = diff @ np.linalg.inv(cov_pred) @ diff
    threshold = p_pred * f_crit * sigma_hat_sq
    
    return mahalanobis <= threshold

# Test points
test_point_1 = np.array([1.7, 0.30])  # plausible: feed=1.7, temp=0.30
test_point_2 = np.array([2.5, 0.70])  # extreme: feed=2.5, temp=0.70

inside_1 = is_inside_ellipse(test_point_1, beta_hat, cov_beta)
inside_2 = is_inside_ellipse(test_point_2, beta_hat, cov_beta)

print(f"\n=== Point-in-Ellipse Test ===")
print(f"Point (β₁=1.7, β₂=0.30): {'INSIDE' if inside_1 else 'OUTSIDE'} the 95% ellipse")
print(f"Point (β₁=2.5, β₂=0.70): {'INSIDE' if inside_2 else 'OUTSIDE'} the 95% ellipse")

# ============================================
# 7. INTERPRETATION SUMMARY
# ============================================

print("\n" + "="*60)
print("FARM INTERPRETATION")
print("="*60)
print(f"""
The 95% confidence ellipse shows the joint uncertainty in our estimates:
- Feed coefficient: {beta_hat[1]:.3f} ± {t_crit*se_beta[1]:.3f} kg/kg
- Temperature coefficient: {beta_hat[2]:.3f} ± {t_crit*se_beta[2]:.3f} kg/°C

Key insights:
1. The ellipse is {'tilted' if abs(cov_beta[1,2]) > 0.1 else 'not tilted'}, 
   indicating that Feed and Temperature effects are {'correlated' if abs(cov_beta[1,2]) > 0.1 else 'independent'}.

2. If you see the ellipse oriented along the diagonal, it means:
   - Pens with high feed also tend to have higher temperatures
   - Or: overestimating one coefficient likely means overestimating the other

3. The ellipse is {'larger' if radius > 1 else 'compact'}, indicating 
   {'high' if radius > 1 else 'low'} uncertainty in our estimates.

Recommendation: Use this ellipse to make joint decisions about 
feed and temperature management, rather than looking at them separately!
""")
