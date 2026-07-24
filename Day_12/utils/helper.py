import os

from utils.config import OUTPUT_DIR, OUTPUT_FILE


def create_output_directory():
    """
    Creates output directory if it doesn't exist.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_to_csv(df):
    """
    Save final dataframe to CSV.
    """

    create_output_directory()

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Final dataset saved to:\n{OUTPUT_FILE}")


def display_shape(df, name):
    """
    Display dataframe information.
    """

    print("-" * 40)
    print(name)
    print("-" * 40)

    print("Rows :", df.shape[0])
    print("Columns :", df.shape[1])

    print()