
class Error(Exception):
    pass


class ValidationError(Error):
    pass


class InvalidKeyError(Error):
    pass


class PaymentRequiredError(Error):
    pass


class UnknownSubaccountError(Error):
    pass


class UnknownTemplateError(Error):
    pass


class ServiceUnavailableError(Error):
    pass


class UnknownMessageError(Error):
    pass


class InvalidTagNameError(Error):
    pass


class InvalidRejectError(Error):
    pass


class UnknownSenderError(Error):
    pass


class UnknownUrlError(Error):
    pass


class UnknownTrackingDomainError(Error):
    pass


class InvalidTemplateError(Error):
    pass


class UnknownWebhookError(Error):
    pass


class UnknownInboundDomainError(Error):
    pass


class UnknownInboundRouteError(Error):
    pass


class UnknownExportError(Error):
    pass


class IPProvisionLimitError(Error):
    pass


class UnknownPoolError(Error):
    pass


class NoSendingHistoryError(Error):
    pass


class PoorReputationError(Error):
    pass


class UnknownIPError(Error):
    pass


class InvalidEmptyDefaultPoolError(Error):
    pass


class InvalidDeleteDefaultPoolError(Error):
    pass


class InvalidDeleteNonEmptyPoolError(Error):
    pass


class InvalidCustomDNSError(Error):
    pass


class InvalidCustomDNSPendingError(Error):
    pass


class MetadataFieldLimitError(Error):
    pass


class UnknownMetadataFieldError(Error):
    pass
