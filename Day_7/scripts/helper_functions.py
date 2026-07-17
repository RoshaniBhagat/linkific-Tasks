import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def create_directory(path):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def save_plot(folder, filename):
    """Save matplotlib plot."""
    create_directory(folder)
    plt.tight_layout()
    plt.savefig(os.path.join(folder, filename))
    print(f"Plot saved: {filename}")
    plt.close()


def print_heading(title):
    """Print formatted heading."""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def separator():
    """Print separator line."""
    print("-" * 60)


def missing_value_summary(df):
    """Return missing value summary."""
    return df.isnull().sum()


def duplicate_summary(df):
    """Return duplicate row count."""
    return df.duplicated().sum()


def numerical_columns(df):
    """Return numerical columns."""
    return df.select_dtypes(include=["number"]).columns


def categorical_columns(df):
    """Return categorical columns."""
    return df.select_dtypes(include=["object"]).columns