import os
from supabase import create_client, Client, AuthApiError
from supabase.client import ClientOptions

supabase_url: str = "123"
#os.environ.get("SUPABASE_URL")
supabase_key: str = "123"
#os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)


def sign_up_user(email: str, password: str, name: str):
    # Sign up the user
     response = supabase.auth.sign_up({
        'email': email,
        'password': password,
        "user_metadata": {
          "name": name
      }
    })
     return "Successfully signed up"


# Replace with actual values
# sign_up_user("peeees@example.com", "secure_password123$R", "User Name")
