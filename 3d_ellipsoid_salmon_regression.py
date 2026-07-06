import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import f
from sklearn.preprocessing import StandardScaler
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
# 3. GENERATE THE 3D CONFIDENCE ELLIPSOID
# ============================================

def get_confidence_ellipsoid(beta_hat, cov_beta, alpha=0.05, n_points=50):
    """
    Generate points on the surface of the confidence ellipsoid.
    
    Returns:
        ellipsoid_points: numpy array of shape (n_points**2, 3)
    """
    p = len(beta_hat) - 1  # number of predictors (excluding intercept)
    n = len(Y)
    
    # F-distribution critical value
    f_crit = f.ppf(1 - alpha, p, n - p - 1)
    
    # Radius of the ellipsoid
    radius = np.sqrt(p * f_crit * sigma_hat_sq)
    
    # Eigen-decomposition of the covariance matrix (for predictors only)
    cov_pred = cov_beta[1:, 1:]  # exclude intercept
    eigvals, eigvecs = np.linalg.eigh(cov_pred)
    
    # Scale eigenvectors by sqrt of eigenvalues and radius
    D = np.diag(np.sqrt(eigvals))
    A = eigvecs @ D * radius
    
    # Generate points on a unit sphere
    u = np.linspace(0, 2 * np.pi, n_points)
    v = np.linspace(0, np.pi, n_points)
    
    points = []
    for theta in u:
        for phi in v:
            # Unit sphere point
            x = np.sin(phi) * np.cos(theta)
            y = np.sin(phi) * np.sin(theta)
            z = np.cos(phi)
            
            # Transform to ellipsoid
            sphere_point = np.array([x, y, z])
            ellipsoid_point = A @ sphere_point + beta_hat[1:]
            points.append(ellipsoid_point)
    
    return np.array(points), f_crit, radius

# Generate ellipsoid points
alpha = 0.05  # 95% confidence
ellipsoid_points, f_crit, radius = get_confidence_ellipsoid(beta_hat, cov_beta, alpha)

# Extract coordinates
feed_ellipse = ellipsoid_points[:, 0]
temp_ellipse = ellipsoid_points[:, 1]

# ============================================
# 4. INTERACTIVE 3D VISUALIZATION WITH PLOTLY
# ============================================

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'scatter3d'}, {'type': 'scatter'}]],
    subplot_titles=('3D Confidence Ellipsoid', '2D Projection (Feed vs Temp)')
)

# --- 3D Ellipsoid ---
fig.add_trace(
    go.Scatter3d(
        x=ellipsoid_points[:, 0],
        y=ellipsoid_points[:, 1],
        z=ellipsoid_points[:, 2],
        mode='markers',
        marker=dict(
            size=2,
            color='rgba(31, 119, 180, 0.6)',
            opacity=0.5
        ),
        name='95% Confidence Ellipsoid'
    ),
    row=1, col=1
)

# Add the estimated coefficients as a point
fig.add_trace(
    go.Scatter3d(
        x=[beta_hat[1]],
        y=[beta_hat[2]],
        z=[0],
        mode='markers',
        marker=dict(
            size=10,
            color='red',
            symbol='x'
        ),
        name='Estimated Coefficients'
    ),
    row=1, col=1
)

# --- 2D Projection (Feed vs Temp) ---
fig.add_trace(
    go.Scatter(
        x=feed_ellipse,
        y=temp_ellipse,
        mode='markers',
        marker=dict(
            size=3,
            color='rgba(31, 119, 180, 0.5)'
        ),
        name='2D Projection'
    ),
    row=1, col=2
)

# Add the estimated coefficients as a point
fig.add_trace(
    go.Scatter(
        x=[beta_hat[1]],
        y=[beta_hat[2]],
        mode='markers',
        marker=dict(
            size=12,
            color='red',
            symbol='x',
            line=dict(width=2)
        ),
        name='Estimated Coefficients'
    ),
    row=1, col=2
)

# Update layout
fig.update_layout(
    title=dict(
        text=f'95% Confidence Ellipsoid for Salmon Regression Coefficients<br>'
             f'F-critical = {f_crit:.3f}, Radius = {radius:.3f}',
        font=dict(size=16)
    ),
    width=1200,
    height=600,
    showlegend=True,
    scene=dict(
        xaxis_title='Feed Coefficient (β₁)',
        yaxis_title='Temperature Coefficient (β₂)',
        zaxis_title='Dummy (for 3D effect)',
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5)
        )
    )
)

fig.update_xaxes(title_text='Feed Coefficient (β₁)', row=1, col=2)
fig.update_yaxes(title_text='Temperature Coefficient (β₂)', row=1, col=2)

# Show the plot
fig.show()

# ============================================
# 5. ADD MARGINAL CONFIDENCE INTERVALS
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

def is_inside_ellipsoid(beta_point, beta_hat, cov_beta, alpha=0.05):
    """
    Check if a given point is inside the confidence ellipsoid.
    """
    p = len(beta_point)
    n = len(Y)
    f_crit = f.ppf(1 - alpha, p, n - p - 1)
    
    diff = beta_point - beta_hat[1:]
    mahalanobis = diff @ np.linalg.inv(cov_beta[1:, 1:]) @ diff
    threshold = p * f_crit * sigma_hat_sq
    
    return mahalanobis <= threshold

# Test points
test_point_1 = np.array([1.7, 0.30])  # plausible: feed=1.7, temp=0.30
test_point_2 = np.array([2.5, 0.70])  # extreme: feed=2.5, temp=0.70

inside_1 = is_inside_ellipsoid(test_point_1, beta_hat, cov_beta)
inside_2 = is_inside_ellipsoid(test_point_2, beta_hat, cov_beta)

print(f"\n=== Point-in-Ellipsoid Test ===")
print(f"Point (β₁=1.7, β₂=0.30): {'INSIDE' if inside_1 else 'OUTSIDE'} the 95% ellipse")
print(f"Point (β₁=2.5, β₂=0.70): {'INSIDE' if inside_2 else 'OUTSIDE'} the 95% ellipse")
