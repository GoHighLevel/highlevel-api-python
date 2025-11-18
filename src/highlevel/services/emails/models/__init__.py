"""Emails Models"""

from .emails import ScheduleDto
from .emails import ScheduleFetchSuccessfulDTO
from .emails import InvalidLocationDTO
from .emails import NotFoundDTO
from .emails import CreateBuilderDto
from .emails import CreateBuilderSuccesfulResponseDto
from .emails import FetchBuilderSuccesfulResponseDto
from .emails import DeleteBuilderSuccesfulResponseDto
from .emails import TemplateSettings
from .emails import IBuilderJsonMapper
from .emails import SaveBuilderDataDto
from .emails import BuilderUpdateSuccessfulDTO
__all__ = ["ScheduleDto", "ScheduleFetchSuccessfulDTO", "InvalidLocationDTO", "NotFoundDTO", "CreateBuilderDto", "CreateBuilderSuccesfulResponseDto", "FetchBuilderSuccesfulResponseDto", "DeleteBuilderSuccesfulResponseDto", "TemplateSettings", "IBuilderJsonMapper", "SaveBuilderDataDto", "BuilderUpdateSuccessfulDTO"]
