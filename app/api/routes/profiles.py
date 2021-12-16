from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.profiles import get_profile_by_username_from_path
from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.database import get_repository
from app.db.repositories.profiles import ProfilesRepository
from app.models.domain.profiles import Profile
from app.models.schemas.profiles import ProfileInResponse
from app.resources import strings


router = APIRouter()


@router.get(
    "/{username}",
    response_model=ProfileInResponse,
    name="profiles:get-profile",
)
async def retrieve_profile_by_username(
    profile: Profile = Depends(get_profile_by_username_from_path),
) -> ProfileInResponse:
    return ProfileInResponse(profile=profile)
