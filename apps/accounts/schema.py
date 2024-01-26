import strawberry_django
import strawberry
from gqlauth.user.queries import UserQueries
from gqlauth.user import arg_mutations as mutations
from typing import List
from . import types
from . import models


@strawberry.type
class Query(UserQueries):
    @strawberry_django.field(description="Get all users")
    def users(self) -> List[types.User]:
        return models.CustomUser.objects.all()

    @strawberry_django.field(description="Get a user by ID")
    def user(self, id: int) -> types.User:
        return models.CustomUser.objects.get(id=id)


@strawberry.type
class Mutation:

    # include what-ever mutations you want.
    verify_token = mutations.VerifyToken.field
    update_account = mutations.UpdateAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field
    password_change = mutations.PasswordChange.field
    # swap_emails = mutations.SwapEmails.field
    # captcha = Captcha.field
    token_auth = mutations.ObtainJSONWebToken.field
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field
    # verify_secondary_email = mutations.VerifySecondaryEmail.field



    @strawberry_django.mutation(description="Create a user")
    def create_user(
        self,
        UserInput: types.UserInput,
    ) -> types.User:
        return models.CustomUser.objects.create_user(
            phone=UserInput.phone,
            email=UserInput.email,
            first_name=UserInput.first_name,
            last_name=UserInput.last_name,
            password=UserInput.password,
        )
