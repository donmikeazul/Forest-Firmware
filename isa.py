# ============== IMPORT MODULES

# NATIVE

# EXTERNAL

# DEVELOPMENT
from forest_firmware.Modules import bill
from forest_firmware.Modules import sat
from forest_firmware.Modules import general

# ============== IMPORT CLASSES

# ============== DEFINE VARIABLES AND CONSTANTS

# VARIABLES

# CONSTANST

# ======================================================== CODE MODULE

# DEFINE FOREST INSTRUCTIONS
instructions = {
	'get_bills_by_date' : bill.get_by_date,
	'get_bills_by_uuid' : bill.get_by_uuid,
	'sat_authentication' : sat.authentication,
	'get_first_bills' : sat.get_first_bills,
	'get_sat_updates' : sat.update,
	'download_from_buffer' : sat.download_from_buffer,
	'get_firmware_status' : general.get_status,
}