from strawberry.field import StrawberryField
from strawberry.annotation import StrawberryAnnotation
from typing import Optional

email_field = StrawberryField(
    type_annotation=StrawberryAnnotation(Optional[str]),
    description="Email",
    python_name="email",
    default=None,
)

phone_field = StrawberryField(
    type_annotation=StrawberryAnnotation(Optional[str]),
    description="Phone",
    python_name="phone",
    default=None,
)
