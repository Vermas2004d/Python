#code for the match case statement
def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Internal Server Error"
        case _: #Default case
            return "Unknown status"
        
print(http_status)

