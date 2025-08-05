import os
from dotenv import load_dotenv

print("Before load_dotenv:")
print(f"ENVIRONMENT: {os.getenv('ENVIRONMENT')}")
print(f"CLERK_SECRET_KEY: {os.getenv('CLERK_SECRET_KEY')}")

load_dotenv()

print("\nAfter load_dotenv:")
print(f"ENVIRONMENT: {os.getenv('ENVIRONMENT')}")
print(f"CLERK_SECRET_KEY: {os.getenv('CLERK_SECRET_KEY')}")

# Test the condition
development_mode = os.getenv("ENVIRONMENT") == "development"
print(f"\nDevelopment mode: {development_mode}")
