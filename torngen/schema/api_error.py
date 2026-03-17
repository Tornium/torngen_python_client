import typing

from .error_access_level_too_low import ErrorAccessLevelTooLow
from .error_api_disabled import ErrorApiDisabled
from .error_api_key_paused import ErrorApiKeyPaused
from .error_backend_error import ErrorBackendError
from .error_category_selection_unavailable_for_interaction_logs import \
    ErrorCategorySelectionUnavailableForInteractionLogs
from .error_closed_temporarily import ErrorClosedTemporarily
from .error_daily_read_limit_reached import ErrorDailyReadLimitReached
from .error_incorrect_category import ErrorIncorrectCategory
from .error_incorrect_id import ErrorIncorrectId
from .error_incorrect_id_entity_relation import ErrorIncorrectIdEntityRelation
from .error_incorrect_key import ErrorIncorrectKey
from .error_incorrect_log_id import ErrorIncorrectLogId
from .error_invalid_stat_requested import ErrorInvalidStatRequested
from .error_ip_blocked import ErrorIpBlocked
from .error_key_change_cooldown import ErrorKeyChangeCooldown
from .error_key_empty import ErrorKeyEmpty
from .error_key_owner_in_federal_jail import ErrorKeyOwnerInFederalJail
from .error_key_read_error import ErrorKeyReadError
from .error_key_temporary_disabled import ErrorKeyTemporaryDisabled
from .error_log_unavailable import ErrorLogUnavailable
from .error_must_migrate_to_crimes_v2 import ErrorMustMigrateToCrimesV2
from .error_must_migrate_to_organized_crimes_v2 import \
    ErrorMustMigrateToOrganizedCrimesV2
from .error_only_available_in_api_v1 import ErrorOnlyAvailableInApiV1
from .error_only_available_in_api_v2 import ErrorOnlyAvailableInApiV2
from .error_only_category_or_stats_allowed import \
    ErrorOnlyCategoryOrStatsAllowed
from .error_race_not_finished import ErrorRaceNotFinished
from .error_too_many_requests import ErrorTooManyRequests
from .error_unknown import ErrorUnknown
from .error_wrong_fields import ErrorWrongFields
from .error_wrong_type import ErrorWrongType

ApiError = (
    ErrorCategorySelectionUnavailableForInteractionLogs
    | ErrorIncorrectLogId
    | ErrorMustMigrateToOrganizedCrimesV2
    | ErrorOnlyCategoryOrStatsAllowed
    | ErrorInvalidStatRequested
    | ErrorClosedTemporarily
    | ErrorOnlyAvailableInApiV2
    | ErrorOnlyAvailableInApiV1
    | ErrorIncorrectCategory
    | ErrorRaceNotFinished
    | ErrorMustMigrateToCrimesV2
    | ErrorApiKeyPaused
    | ErrorBackendError
    | ErrorAccessLevelTooLow
    | ErrorLogUnavailable
    | ErrorDailyReadLimitReached
    | ErrorKeyTemporaryDisabled
    | ErrorKeyReadError
    | ErrorKeyChangeCooldown
    | ErrorKeyOwnerInFederalJail
    | ErrorApiDisabled
    | ErrorIpBlocked
    | ErrorIncorrectIdEntityRelation
    | ErrorIncorrectId
    | ErrorTooManyRequests
    | ErrorWrongFields
    | ErrorWrongType
    | ErrorIncorrectKey
    | ErrorKeyEmpty
    | ErrorUnknown
)
