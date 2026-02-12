class KVDTError(Exception):
    """Base class for all KVDT related errors."""
    pass

class KVDTReaderError(KVDTError):
    """Raised when the KVDT file structure is fundamentally malformed."""
    def __init__(self, message, line_nbr=None):
        self.line_nbr = line_nbr
        full_message = f"Line {line_nbr}: {message}" if line_nbr else message
        super().__init__(full_message)

class KVDTParserError(KVDTError):
    """Raised when the KVDT sentence structure is invalid."""
    pass

class KVDTValidationError(KVDTError):
    """Raised for field-level validation failures."""
    def __init__(self, message, field_id=None, line_nbr=None, satz_type=None):
        self.field_id = field_id
        self.line_nbr = line_nbr
        self.satz_type = satz_type
        
        context = []
        if satz_type:
            context.append(f"Satz {satz_type}")
        if line_nbr:
            context.append(f"Line {line_nbr}")
        if field_id:
            context.append(f"Field {field_id}")
        
        ctx_str = f"[{', '.join(context)}] " if context else ""
        super().__init__(f"{ctx_str}{message}")
