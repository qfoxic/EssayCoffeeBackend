import re

ORDER_MAIL = """
Dear %(first_name)s 

Thank you for ordering at %(domain)s. We will assign your order to the best writer available as soon as 

possible and will let you know via email.

Regards,

Administration
"""

NEW_PROFILE_EMAIL = """ 
Dear %(first_name)s 

Thank you for registering at %(domain)s.
Your username: %(username)s
Your email: %(email)s

Regards,
Administration
"""

NEW_PROFILE_SUBJECT = 'Thanks for registering.'
ORDER_MAIL_SUBJECT = 'Thanks for ordering.'
DELETE_ORDER_SUBJECT = 'Your order has been deleted.'
DELETE_ORDER_EMAIL = """ 
Dear %(first_name)s 

Your order "%(order_title)s" with id "%(order_id)s" has been deleted.

Regards,
Administration
"""

UPDATE_PASSWORD_EMAIL = """ 
Dear %(first_name)s 

Your password has been updated sucessfully.

Regards,
Administration
"""

ORDER_FINISHED_EMAIL = """ 
Dear %(first_name)s 

Your order "%(order_title)s" with id "%(order_id)s" has been completed.

Regards,
Administration
"""

#EMAIL_HOST = 'smtp.ukr.net'
#EMAIL_HOST_PASSWORD = 'QAZqaz1983'
#EMAIL_HOST_USER = 'workforum@ukr.net'
#EMAIL_PORT = 465

EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_HOST_PASSWORD = 'ArjbUpVfD8Slt91OAy11bInlmzcIH+NJUxYe8jz/LVvr'
EMAIL_HOST_USER = 'AKIAILRHCFXQWXJEGIVA'
EMAIL_PORT = 465

#ADMIN_EMAIL = 'workforum@ukr.net'#'no-reply@essaycoffee.com'
ADMIN_EMAIL = 'no-reply@essaycoffee.com'
INFO_EMAIL = 'info@essaycoffee.com'
ADMIN_DOMAIN = 'www.essaycoffee.com'

# Settings related variables.
CONFIG_PATH = 'config'
GLOBAL_MODULE_NAME = 'global'
CONFIG_FILE_ENDING = '.settings.yml'

DEFAULT_SKIN_PREFIX = 'default'

# Some usefull urls
LOGIN_URL = 'login/'

# Decimal number settings
DECIMAL_DIGITS = 6
DECIMAL_PLACES = 2


# Max length of a title
TITLE_MAX_LEN = 100

# Max len of typical overview string
MAX_STRING_LEN = 500
INSTRUCTION_MAX_LEN = 10000
MAX_FILE_LEN = 50 * 1024 * 1024 # 50 MB

# Task related statuses.
UNPROCESSED = 7
PROCESSING = 1
REJECTED = 2
COMPLETED = 3
DRAFT = 4
SUSPICIOUS = 5
SENT = 6

UNASSIGNED_ORDER = '0'
ASSIGNED_ORDER = '1'

TASK_STATUSES = (
  (PROCESSING, 'PROCESSING'),
  (UNPROCESSED, 'UNPROCESSED'),
  (REJECTED, 'REJECTED'),
  (SUSPICIOUS, 'SUSPICIOUS'),
  (DRAFT, 'DRAFT'),
  (SENT, 'SENT'),
  (COMPLETED, 'COMPLETED'))

TASK_STATUSES_DICT = dict(TASK_STATUSES)

# Payment systems.
LIQPAY = 1 

LIQ_PUB_KEY = 'i77735892077'
LIQ_PRIV_KEY = 'JGTGKOKgrHzSr5mEVD6CAaik3acoR4cwqPF529BN'

TWOCHECKOUT = 2
TWOSID = '202362386'
TWO_PUB_KEY = '4E238020-3AE1-11E4-84E6-7C8C3A5D4FFE'
TWO_PRIV_KEY = '4E2380DE-3AE1-11E4-84E6-7C8C3A5D4FFE'
TWO_USERNAME = 'essayapi'
TWO_PASSWORD = 'QAZqaz19831234567890'

PAYMENT_SYSTEMS = (
  (LIQPAY, 'Liqpay'),
  (TWOCHECKOUT, '2Checkout'),
)

PAYMENT_SYSTEMS_DICT = dict(PAYMENT_SYSTEMS)

PAID = 0
UNPAID = 1
IN_PROCESS = 2
UNDERPAID = 3

PAYMENT_STATUS = (
  (UNPAID, 'Unpaid'),
  (PAID, 'Paid'),
  (IN_PROCESS, 'In process'),
  (UNDERPAID, 'Underpaid')
)
PAYMENT_STATUS_DICT = dict(PAYMENT_STATUS)

# Main purpose of a table is do not allow to set
# inconsistent status to an order.
# Before status will be set we have to check whether
# according record is here and status to set is within allowed.
STATUS_SWITCH_TABLE = {
  PROCESSING: [SUSPICIOUS,REJECTED,SENT],
  UNPROCESSED: [UNPROCESSED,PROCESSING,SUSPICIOUS,REJECTED],
  SUSPICIOUS: [PROCESSING,REJECTED],
  DRAFT: [DRAFT,UNPROCESSED],
  SENT: [COMPLETED]
}


CUSTOMER_GROUP = 'customer'
WRITER_GROUP = 'writer'
ADMIN_GROUP = 'admin'
EDITOR_GROUP = 'editor'

# Allow user to edit orders
CAN_EDIT = 'can_edit'
CAN_DELETE = 'can_delete'

CAN_COMMENT = 'can_comment'
CAN_SEE_COMMENTS = 'can_see_comments'
CAN_MESSAGE = 'can_message'

# Allow owners to submit their orders.
CAN_SUBMIT = 'can_submit'

# Allow to do approve, reject, suspect 
CAN_APPROVE = 'can_approve'
CAN_REJECT = 'can_reject'
CAN_SUSPECT = 'can_suspect'

# Allow for writers to complete a user.
CAN_COMPLETE = 'can_complete'

CAN_SEND = 'can_send'
CAN_UPLOAD = 'can_upload'

# Allow admins to put reports on tasks
CAN_REPORT = 'can_report'

# Whether anyone can lock a task.
CAN_LOCK = 'can_lock'
CAN_UNLOCK = 'can_unlock'
CAN_REVISION = 'can_revision'

# Whether users can change visibility for an upload
CAN_CH_VISIBILITY = 'can_visibility'

# 3d table with different permissions for each action and each group.
# If specific permissions wasn't found here then it is concerned as not allowed.
PERMISSIONS_TABLE = {
  'message': {
  CUSTOMER_GROUP+str(DRAFT)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(DRAFT)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(DRAFT)+CAN_DELETE: 1,
  ADMIN_GROUP+str(DRAFT)+CAN_EDIT: 1,

  # Unprocessed permissions.
  ADMIN_GROUP+str(UNPROCESSED)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_DELETE: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(UNPROCESSED)+CAN_MESSAGE: 1,

  # Active or in progress permissions.
  ADMIN_GROUP+str(PROCESSING)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_DELETE: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(PROCESSING)+CAN_MESSAGE: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_MESSAGE: 1,
  WRITER_GROUP+str(PROCESSING)+CAN_MESSAGE: 1,

  # Suspicious permissions.
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_DELETE: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(SUSPICIOUS)+CAN_MESSAGE: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_MESSAGE: 1,
  WRITER_GROUP+str(SUSPICIOUS)+CAN_MESSAGE: 1,

  # Rejected 
  ADMIN_GROUP+str(REJECTED)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_DELETE: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(REJECTED)+CAN_MESSAGE: 1,
  EDITOR_GROUP+str(REJECTED)+CAN_MESSAGE: 1,
  WRITER_GROUP+str(REJECTED)+CAN_MESSAGE: 1,

  # Completed
  ADMIN_GROUP+str(COMPLETED)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_DELETE: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(COMPLETED)+CAN_MESSAGE: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_MESSAGE: 1,
  WRITER_GROUP+str(COMPLETED)+CAN_MESSAGE: 1,

  # Send
  ADMIN_GROUP+str(SENT)+CAN_MESSAGE: 1,
  ADMIN_GROUP+str(SENT)+CAN_DELETE: 1,
  ADMIN_GROUP+str(SENT)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(SENT)+CAN_MESSAGE: 1,
  EDITOR_GROUP+str(SENT)+CAN_MESSAGE: 1,
  WRITER_GROUP+str(SENT)+CAN_MESSAGE: 1,
  },
  'upload': {
  # Draft permissions.
  CUSTOMER_GROUP+str(DRAFT)+CAN_DELETE: 1,
  CUSTOMER_GROUP+str(DRAFT)+CAN_UPLOAD: 1,
  
  # Unprocessed permissions.
  CUSTOMER_GROUP+str(UNPROCESSED)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_UPLOAD: 1,
  EDITOR_GROUP+str(UNPROCESSED)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_DELETE: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_CH_VISIBILITY: 1,
  EDITOR_GROUP+str(UNPROCESSED)+CAN_CH_VISIBILITY: 1,
  EDITOR_GROUP+str(UNPROCESSED)+CAN_DELETE: 1,

  # Active or in progress permissions.
  CUSTOMER_GROUP+str(PROCESSING)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_UPLOAD: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_UPLOAD: 1,
  WRITER_GROUP+str(PROCESSING)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_CH_VISIBILITY: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_DELETE: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_DELETE: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_CH_VISIBILITY: 1,

  # Suspicious permissions.
  CUSTOMER_GROUP+str(SUSPICIOUS)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_UPLOAD: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_CH_VISIBILITY: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_DELETE: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_CH_VISIBILITY: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_DELETE: 1,

  # Rejected 
  EDITOR_GROUP+str(REJECTED)+CAN_CH_VISIBILITY: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_CH_VISIBILITY: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_DELETE: 1,

  # Completed
  ADMIN_GROUP+str(COMPLETED)+CAN_CH_VISIBILITY: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_DELETE: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_CH_VISIBILITY: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_DELETE: 1,
  WRITER_GROUP+str(COMPLETED)+CAN_UPLOAD: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_UPLOAD: 1,

  # Send
  CUSTOMER_GROUP+str(SENT)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(SENT)+CAN_UPLOAD: 1,
  WRITER_GROUP+str(SENT)+CAN_UPLOAD: 1,
  EDITOR_GROUP+str(SENT)+CAN_UPLOAD: 1,
  ADMIN_GROUP+str(SENT)+CAN_CH_VISIBILITY: 1,
  ADMIN_GROUP+str(SENT)+CAN_DELETE: 1,
  EDITOR_GROUP+str(SENT)+CAN_CH_VISIBILITY: 1,
  EDITOR_GROUP+str(SENT)+CAN_DELETE: 1,
  },
  # Permissions for a task.
  'task': {
  # Draft permissions.
  CUSTOMER_GROUP+str(DRAFT)+CAN_SUBMIT: 1,
  CUSTOMER_GROUP+str(DRAFT)+CAN_EDIT: 1,
  CUSTOMER_GROUP+str(DRAFT)+CAN_DELETE: 1,
  
  # Unprocessed permissions.
  ADMIN_GROUP+str(UNPROCESSED)+CAN_EDIT: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_APPROVE: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_REJECT: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_SUSPECT: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_REPORT: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_LOCK: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_UNLOCK: 1,
  ADMIN_GROUP+str(UNPROCESSED)+CAN_REVISION: 1,

  # Active or in progress permissions.
  ADMIN_GROUP+str(PROCESSING)+CAN_EDIT: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_LOCK: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_UNLOCK: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_REJECT: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_REPORT: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_SUSPECT: 1,
  ADMIN_GROUP+str(PROCESSING)+CAN_REVISION: 1,
  WRITER_GROUP+str(PROCESSING)+CAN_LOCK: 1,
  WRITER_GROUP+str(PROCESSING)+CAN_SEND: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_LOCK: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_REPORT: 1,
  EDITOR_GROUP+str(PROCESSING)+CAN_UNLOCK: 1,
  
  # Suspicious permissions.
  CUSTOMER_GROUP+str(SUSPICIOUS)+CAN_EDIT: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_EDIT: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_LOCK: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_UNLOCK: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_REJECT: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_REPORT: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_APPROVE: 1,
  ADMIN_GROUP+str(SUSPICIOUS)+CAN_REVISION: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_LOCK: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_REPORT: 1,
  EDITOR_GROUP+str(SUSPICIOUS)+CAN_UNLOCK: 1,

  # Rejected.
  ADMIN_GROUP+str(REJECTED)+CAN_EDIT: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_LOCK: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_UNLOCK: 1,
  ADMIN_GROUP+str(REJECTED)+CAN_REPORT: 1,
  EDITOR_GROUP+str(REJECTED)+CAN_REPORT: 1,
  EDITOR_GROUP+str(REJECTED)+CAN_LOCK: 1,
  EDITOR_GROUP+str(REJECTED)+CAN_UNLOCK: 1,

  # Completed
  ADMIN_GROUP+str(COMPLETED)+CAN_EDIT: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_LOCK: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_UNLOCK: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_REPORT: 1,
  ADMIN_GROUP+str(COMPLETED)+CAN_REVISION: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_REPORT: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_LOCK: 1,
  EDITOR_GROUP+str(COMPLETED)+CAN_UNLOCK: 1,

  # Send
  ADMIN_GROUP+str(SENT)+CAN_LOCK: 1,
  ADMIN_GROUP+str(SENT)+CAN_UNLOCK: 1,
  EDITOR_GROUP+str(SENT)+CAN_LOCK: 1,
  EDITOR_GROUP+str(SENT)+CAN_UNLOCK: 1,
  EDITOR_GROUP+str(SENT)+CAN_COMPLETE: 1,
  EDITOR_GROUP+str(SENT)+CAN_REPORT: 1,
  ADMIN_GROUP+str(SENT)+CAN_REPORT: 1,
  }
}

def CheckPermissions(user, entity, action, entity_type='task'):
  try:
    if entity_type == 'message':
      entity = entity if entity.__class__.__name__ == 'Task' else entity.mtask
    elif entity_type == 'upload':
      entity = entity if entity.__class__.__name__ == 'Task' else entity.ftask
    group = user.groups.values_list('name')[0][0]
    status = entity.status
  except:
    status, group = '', ''

  return PERMISSIONS_TABLE[entity_type].get(group+str(status)+action) is not None

def CheckPermissionTmpl(entity, action):
  status = entity.status
  group = CUSTOMER_GROUP
  return PERMISSIONS_TABLE[entity.__class__.__name__.lower()].get(group+str(status)+action) is not None
  

MALE = 0
FEMALE = 1
GENDER = ((MALE, 'Mr.'),
          (FEMALE, 'Ms.'))

COUNTRIES = (
  ('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'),
  ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'),
  ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'),
  ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'),
  ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'),
  ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'),
  ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'),
  ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'),
  ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'),
  ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'),
  ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'),
  ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'),
  ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'),
  ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'),
  ('CG', 'Congo'),  ('CD', 'Congo, Democratic Republic'),  ('CK', 'Cook Islands'),
  ('CR', 'Costa Rica'),  ('CI', 'Cote d\'Ivoire'),  ('HR', 'Croatia'),  ('CY', 'Cyprus'),
  ('CZ', 'Czech Republic'),  ('DK', 'Denmark'),  ('DJ', 'Djibouti'),
  ('DM', 'Dominica'),  ('DO', 'Dominican Republic'),  ('TL', 'East Timor'),
  ('EC', 'Ecuador'),  ('EG', 'Egypt'),  ('SV', 'El Salvador'),
  ('GQ', 'Equatorial Guinea'),  ('ER', 'Eritrea'),  ('EE', 'Estonia'),
  ('ET', 'Ethiopia'),  ('FK', 'Falkland Islands (Malvinas)'),
  ('FO', 'Faroe Islands'),  ('FJ', 'Fiji'),  ('FI', 'Finland'),  ('FR', 'France'),
  ('GF', 'French Guiana'),  ('PF', 'French Polynesia'),
  ('TF', 'French Southern Territories'),  ('GA', 'Gabon'),  ('GM', 'Gambia'),
  ('GE', 'Georgia'),  ('DE', 'Germany'),  ('GH', 'Ghana'),  ('GI', 'Gibraltar'),
  ('GR', 'Greece'),  ('GL', 'Greenland'),  ('GD', 'Grenada'),
  ('GP', 'Guadeloupe'),  ('GU', 'Guam'),  ('GT', 'Guatemala'),  ('GN', 'Guinea'),
  ('GW', 'Guinea-Bissau'),  ('GY', 'Guyana'),  ('HT', 'Haiti'),
  ('HM', 'Heard and McDonald Islands'),  ('HN', 'Honduras'),  ('HK', 'Hong Kong'),
  ('HU', 'Hungary'),  ('IS', 'Iceland'),  ('IN', 'India'),  ('ID', 'Indonesia'),
  ('IQ', 'Iraq'),  ('IE', 'Ireland'),  ('IL', 'Israel'),  ('IT', 'Italy'),
  ('JM', 'Jamaica'),  ('JP', 'Japan'),  ('JO', 'Jordan'),
  ('KZ', 'Kazakhstan'),  ('KE', 'Kenya'),  ('KI', 'Kiribati'),  ('KW', 'Kuwait'),
  ('KG', 'Kyrgyzstan'),  ('LA', 'Lao People\'s Democratic Republic'),
  ('LV', 'Latvia'),  ('LB', 'Lebanon'),  ('LS', 'Lesotho'),  ('LR', 'Liberia'),
  ('LY', 'Libya'),  ('LI', 'Liechtenstein'),  ('LT', 'Lithuania'),
  ('LU', 'Luxembourg'),  ('MO', 'Macau'),  ('MK', 'Macedonia'),  ('MG', 'Madagascar'),
  ('MW', 'Malawi'),  ('MY', 'Malaysia'),  ('MV', 'Maldives'),  ('ML', 'Mali'),
  ('MT', 'Malta'),  ('MH', 'Marshall Islands'),  ('MQ', 'Martinique'),
  ('MR', 'Mauritania'),  ('MU', 'Mauritius'),  ('YT', 'Mayotte'),  ('MX', 'Mexico'),
  ('FM', 'Micronesia'),  ('MD', 'Moldova'),  ('MC', 'Monaco'),  ('MN', 'Mongolia'),
  ('MS', 'Montserrat'),  ('MA', 'Morocco'), ('MZ', 'Mozambique'),  ('NA', 'Namibia'),
  ('NR', 'Nauru'),  ('NP', 'Nepal'),  ('NL', 'Netherlands'),
  ('AN', 'Netherlands Antilles'),  ('NC', 'New Caledonia'),  ('NZ', 'New Zealand'),
  ('NI', 'Nicaragua'),  ('NE', 'Niger'),  ('NG', 'Nigeria'),  ('NU', 'Niue'),
  ('NF', 'Norfolk Island'),  ('MP', 'Northern Mariana Islands'),  ('NO', 'Norway'),
  ('OM', 'Oman'), ('PK', 'Pakistan'),  ('PW', 'Palau'),  ('PS', 'Palestinian Territory'),
  ('PA', 'Panama'),  ('PG', 'Papua New Guinea'),  ('PY', 'Paraguay'),  ('PE', 'Peru'),
  ('PH', 'Philippines'),  ('PN', 'Pitcairn'),  ('PL', 'Poland'),  ('PT', 'Portugal'),
  ('PR', 'Puerto Rico'),  ('QA', 'Qatar'),  ('RE', 'Reunion'),  ('RO', 'Romania'),
  ('RU', 'Russian Federation'),  ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'),
  ('LC', 'Saint Lucia'),  ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'),
  ('SM', 'San Marino'),  ('ST', 'Sao Tome and Principe'),  ('SA', 'Saudi Arabia'),
  ('SN', 'Senegal'),  ('CS', 'Serbia and Montenegro'),  ('SC', 'Seychelles'), 
  ('SL', 'Sierra Leone'),  ('SG', 'Singapore'),  ('SK', 'Slovakia'), ('SI', 'Slovenia'),
  ('SB', 'Solomon Islands'),  ('SO', 'Somalia'),  ('ZA', 'South Africa'),
  ('GS', 'South Georgia and The South Sandwich Islands'),  ('KR', 'South Korea'),
  ('ES', 'Spain'),  ('LK', 'Sri Lanka'),  ('SH', 'St. Helena'),
  ('PM', 'St. Pierre and Miquelon'), ('SR', 'Suriname'),
  ('SJ', 'Svalbard and Jan Mayen Islands'),  ('SZ', 'Swaziland'),  ('SE', 'Sweden'),
  ('CH', 'Switzerland'),  ('TW', 'Taiwan'),  ('TJ', 'Tajikistan'),  ('TZ', 'Tanzania'),
  ('TH', 'Thailand'),  ('TG', 'Togo'),  ('TK', 'Tokelau'),  ('TO', 'Tonga'),
  ('TT', 'Trinidad and Tobago'),  ('TN', 'Tunisia'),  ('TR', 'Turkey'),
  ('TM', 'Turkmenistan'),  ('TC', 'Turks and Caicos Islands'),  ('TV', 'Tuvalu'),
  ('UG', 'Uganda'),  ('UA', 'Ukraine'),  ('AE', 'United Arab Emirates'),
  ('GB', 'United Kingdom'),  ('US', 'United States'),
  ('UM', 'United States Minor Outlying Islands'),  ('UY', 'Uruguay'),
  ('UZ', 'Uzbekistan'),  ('VU', 'Vanuatu'),  ('VA', 'Vatican'),  ('VE', 'Venezuela'),
  ('VN', 'Viet Nam'),  ('VG', 'Virgin Islands (British)'), 
  ('VI', 'Virgin Islands (U.S.)'),  ('WF', 'Wallis and Futuna Islands'), 
  ('EH', 'Western Sahara'),  ('YE', 'Yemen'),
  ('ZM', 'Zambia'),  ('ZW', 'Zimbabwe'))

MAX_PAGE_PRICE = 48.00
ITEMS_PERCENTS = {
  # Max 33%
  'assigments': {
    'es': 0.2, 're': 0.1, 'ab': 0.15,
    'an': 0.14, 'rw': 0.13, 'cs': 0.18
  },
  # Max 33%
  'levels': {
    'hs': 0.24, 'co': 0.26, 'un': 0.28,
    'ms': 0.3, 'ph': 0.33
  },
  # Max 33%.
  'urgency': {
    21600: 0.33, 43200: 0.32, 86400: 0.31, 172800: 0.3,
    259200: 0.29, 518400: 0.28, 1036800: 0.27,
    2073600: 0.26
  },
  # single 100%, double 0%.
  'spacing': {
    1: 1.0,
    2: 0.0
  }
    
}

DISCIPLINES = (
  (0, 'Please select'),
  ('hs', 'History'),
  ('ln', 'Linguistics'),
  ('lt', 'Literature'),
  ('pa', 'Performing arts'),
  ('ph', 'Philosophy'),
  ('rg', 'Religion'),
  ('va', 'Visual arts'),
  ('an', 'Anthropology'),
  ('ar', 'Archaeology'),
  ('as', 'Area studies'),
  ('cu', 'Cultural and ethnic studies'),
  ('ec', 'Economics'),
  ('gs', 'Gender and sexuality studies'),
  ('ge', 'Geography'),
  ('ps', 'Political science'),
  ('py', 'Psychology'),
  ('so', 'Sociology'),
  ('ss', 'Space sciences'),
  ('es', 'Earth sciences'),
  ('ls', 'Life sciences'),
  ('ch', 'Chemistry'))


ASSIGMENTS = (
  (0, 'Please select'),
  ('0.0', 'Essay'),
  ('1.0', 'Online Test'),
  ('2.0', 'Term paper'),
  ('2.1', 'Research paper'),
  ('2.2', 'Book Report'),
  ('2.3', 'Book Review'),
  ('2.4', 'Coursework'),
  ('2.5', 'Research proposal'),
  ('2.6', 'Questions-Answers'),
  ('2.7', 'Annotated Bibliography'),
  ('3.0', 'Dissertation'),
  ('3.1', 'Thesis'),
  ('3.2', 'Dissertation chapter - Abstract'),
  ('3.3', 'Dissertation chapter - Introduction'),
  ('3.4', 'Dissertation chapter - Hypothesis'),
  ('3.5', 'Dissertation chapter - Literature review'),
  ('3.6', 'Dissertation chapter - Methodology'),
  ('3.7', 'Dissertation chapter - Results'),
  ('3.8', 'Dissertation chapter - Discussion'),
  ('3.9', 'Dissertation chapter - Conclusion'),
  ('3.10', 'Thesis Proposal'),
  ('3.11', 'Thesis/dissertation chapter'),
  ('4.0', 'Formatting'),
  ('5.0', 'Editing'),
  ('6.0', 'Proofreading'),
  ('7.0', 'Rewriting'),
  ('8.0', 'Powerpoint Presentation'))  

LEVELS = (
  (0, 'Please select'),
  (1, 'High School'),
  (2, 'College'),
  (3, 'University'),
  (4, 'Master\'s'),
  (5, 'PHD'),
  (6, 'Undergraduate'))

LEVELS5_HCUMP = dict(LEVELS[1:6])
LEVELS3_EMP = dict((LEVELS[6], LEVELS[4], LEVELS[5]))
LEVELS5_HCEMP = dict((LEVELS[1], LEVELS[2], LEVELS[6], LEVELS[4], LEVELS[5]))
LEVELS5_HCEM = dict((LEVELS[1], LEVELS[2], LEVELS[6], LEVELS[4]))

# Urgency is more convenient to represent as time in seconds and label
URGENCY = (
  (0, 'Please select'),
  (10800, '3 hours'),
  (21600, '6 hours'),
  (28800, '8 hours'),
  (43200, '12 hours'),
  (86400, '24 hours'),
  (172800, '48 hours'),
  (259200, '3 days'),
  (345600, '4 days'),
  (432000, '5 days'),
  (604800, '7 days'),
  (864000, '10 days'),
  (950400, '11 days'),
  (1209600, '14 days'),
  (1814400, '21 days'),
  (2592000, '1 month'),
  (5184000, '2 months'))

URGENCY_11_DAYS = dict((URGENCY[1], URGENCY[2], URGENCY[3],
                       URGENCY[4], URGENCY[5], URGENCY[6], URGENCY[7],
                       URGENCY[8], URGENCY[10], URGENCY[12]))
URGENCY_6_HOURS = dict((URGENCY[1], URGENCY[2], URGENCY[3]))
URGENCY_3_6_HOURS = dict((URGENCY[1], URGENCY[2]))
URGENCY_2_MONTHS = dict((URGENCY[6], URGENCY[9], URGENCY[11], URGENCY[13],
                        URGENCY[14], URGENCY[15], URGENCY[16]))
URGENCY_10_DAYS = dict((URGENCY[1], URGENCY[2], URGENCY[4], URGENCY[5], URGENCY[6],
                        URGENCY[7], URGENCY[8], URGENCY[10], URGENCY[11]))

SPACING = (
  (0, 'Please select'),
  (1, 'Single'),
  (2, 'Double'))

STYLES = (
  (0, 'Please select'),
  (1, 'MLA'),
  (2, 'APA'),
  (3, 'Chicago'),
  (4, 'Turabian'),
  (5, 'Harvard'),
  (6, 'other'))



PRICELIST = [
  {
    "assigments": ["Essay"],
    "urgencies": URGENCY_11_DAYS,
    "levels": LEVELS5_HCUMP, 
    "prices": {
        950400: {1:12.99, 2:15.99, 3:17.99, 4:22.99, 5:27.99},
        604800: {1:14.99, 2:16.99, 3:18.99, 4:24.99, 5:29.99},
        345600: {1:16.99, 2:18.99, 3:19.99, 4:25.99, 5:32.99},
        259200: {1:17.99, 2:19.99, 3:21.99, 4:29.99, 5:34.99},
        172800: {1:19.99, 2:22.99, 3:25.99, 4:31.99, 5:41.99},
        86400: {1:21.99, 2:24.99, 3:27.99, 4:36.99, 5:47.99},
        43200: {1:23.99, 2:28.99, 3:35.99, 4:43.99, 5:49.99},
        28800: {1:24.99, 2:30.99, 3:36.99, 4:44.99, 5:0},
        21600: {1:34.99, 2:38.99, 3:43.99, 4:0, 5:0},
        10800: {1:48.99, 2:54.99, 3:61.99, 4:0, 5:0}
    }
  },
  {
    "assigments": ["Online Test"],
    "urgencies": URGENCY_3_6_HOURS,
    "levels": LEVELS5_HCUMP,
    "prices": {
        21600: {1:34.99, 2:38.99, 3:43.99, 4:0, 5:0},
        10800: {1:48.99, 2:54.99, 3:61.99, 4:0, 5:0}
      }
  },
  {
    "assigments": ["Term paper", "Research paper", "Book Report", "Book Review", "Coursework", "Research proposal", "Questions-Answers", "Annotated Bibliography"],
    "urgencies": URGENCY_11_DAYS,
    "levels": LEVELS5_HCUMP,
    "prices":  {
        950400: {1:12.99, 2:15.99, 3:17.99, 4:22.99, 5:27.99},
        604800: {1:14.99, 2:16.99, 3:18.99, 4:24.99, 5:29.99},
        345600: {1:16.99, 2:18.99, 3:19.99, 4:25.99, 5:32.99},
        259200: {1:17.99, 2:19.99, 3:21.99, 4:29.99, 5:34.99},
        172800: {1:19.99, 2:22.99, 3:25.99, 4:31.99, 5:41.99},
        86400: {1:21.99, 2:24.99, 3:27.99, 4:36.99, 5:47.99},
        43200: {1:23.99, 2:28.99, 3:35.99, 4:43.99, 5:49.99},
        28800: {1:24.99, 2:30.99, 3:36.99, 4:44.99, 5:0},
        21600: {1:34.99, 2:38.99, 3:43.99, 4:0, 5:0},
        10800: {1:48.99, 2:54.99, 3:61.99, 4:0, 5:0}
      }
  },
  {
    "assigments": ["Dissertation", "Thesis", "Dissertation chapter - Abstract", "Dissertation chapter - Introduction",
                   "Dissertation chapter - Hypothesis", "Dissertation chapter - Literature review",
                   "Dissertation chapter - Methodology", "Dissertation chapter - Results", "Dissertation chapter - Discussion",
                   "Dissertation chapter - Conclusion", "Thesis Proposal", "Thesis/dissertation chapter"],
    "urgencies": URGENCY_2_MONTHS,
    "levels": LEVELS3_EMP,
    "prices": {
        5184000: {6:18, 4:23, 5:26},
        2592000: {6:19, 4:24, 5:27},
        1814400: {6:21, 4:26, 5:28},
        1209600: {6:24, 4:28, 5:31},
        864000: {6:27, 4:31, 5:35},
        432000: {6:30, 4:35, 5:40},
        172800: {6:40, 4:45, 5:50}
      }
  },
  {
    "assigments": ["Formatting"],
    "urgencies": URGENCY_10_DAYS,
    "levels": LEVELS5_HCEMP,
    "prices": {
        864000: {1:1, 2:1.5, 6:2, 4:2.5, 5:3},
        604800: {1:2.5, 2:3, 6:3.5, 4:4, 5:4.5},
        345600: {1:3, 2:3.5, 6:4, 4:4.5, 5:5},
        259200: {1:3.5, 2:4, 6:4.5, 4:5, 5:5.5},
        172800: {1:4, 2:4.5, 6:5, 4:5.5, 5:6},
        86400: {1:4.5, 2:5, 6:5.5, 4:6, 5:6.5},
        43200: {1:5.5, 2:6, 6:6.5, 4:7, 5:7.5},
        21600: {1:6.5, 2:7, 6:7.5, 4:8, 5:8.5},
        10800: {1:8.5, 2:9, 6:9.5, 4:10, 5:10.5}
      }
  },
  {
    "assigments": ["Editing"],
    "urgencies": URGENCY_11_DAYS,
    "levels": LEVELS5_HCEM,
    "prices": {
        1209600: {1:5.99, 2:6.99, 6:7.99, 4:11.99},
        864000: {1:6.99, 2:7.99, 6:8.99, 4:12.99},
        518400: {1:7.99, 2:8.99, 6:9.99, 4:13.99},
        259200: {1:8.99, 2:9.99, 6:10.99, 4:14.99},
        172800: {1:9.99, 2:10.99, 6:12.99, 4:15.99},
        86400: {1:10.99, 2:12.99, 6:14.99, 4:18.99},
        43200: {1:12.99, 2:15.99, 6:18.99, 4:21.99}, 
        28800: {1:13.99, 2:16.99, 6:19.99, 4:22.99},
        21600: {1:14.99, 2:17.99, 6:20.99, 4:23.99},
        10800: {1:15.99, 2:18.99, 6:21.99, 4:24.99}
      }
  },
  {
    "assigments": ["Proofreading"],
    "urgencies": URGENCY_11_DAYS,
    "levels": LEVELS5_HCEM, 
    "prices": {
        950400: {1:4.99, 2:5.99, 6:6.99, 4:8.99},
        604800: {1:5.99, 2:6.99, 6:7.99, 4:9.99},
        345600: {1:5.99, 2:7.99, 6:8.99, 4:10.99},
        259200: {1:6.99, 2:7.99, 6:9.99, 4:11.99},
        172800: {1:6.99, 2:8.99, 6:10.99, 4:12.99},
        86400: {1:7.99, 2:9.99, 6:11.99, 4:13.99},
        43200: {1:7.99, 2:9.99, 6:11.99, 4:14.99},
        28800: {1:8.99, 2:10.99, 6:12.99, 4:15.99},
        21600: {1:9.99, 2:11.99, 6:13.99, 4:16.99},
        10800: {1:11.99, 2:13.99, 6:15.99, 4:18.99}
      }
  },
  {
    "assigments": ["Rewriting"],
    "urgencies": URGENCY_11_DAYS,
    "levels": LEVELS5_HCEMP,
    "prices": {
        2592000: {1:5.99, 2:6.99, 6:8.99, 4:11.99, 5:15.99},
        1814400: {1:6.99, 2:7.99, 6:9.99, 4:14.99, 5:21.99},
        950400: {1:7.99, 2:8.99, 6:10.99, 4:15.99, 5:23.99},
        604800: {1:8.99, 2:9.99, 6:12.99, 4:16.99, 5:22.99},
        345600: {1:9.99, 2:11.99, 6:13.99, 4:18.99, 5:25.99},
        259200: {1:10.99, 2:12.99, 6:14.99, 4:20.99, 5:26.99},
        172800: {1:12.99, 2:13.99, 6:17.99, 4:22.99, 5:29.99},
        86400: {1:14.99, 2:17.99, 6:19.99, 4:25.99, 5:33.99},
        43200: {1:16.99, 2:21.99, 6:25.99, 4:31.99, 5:39.99},
        28800: {1:17.99, 2:22.99, 6:26.99, 4:32.99, 5:40.99},
        21600: {1:18.99, 2:23.99, 6:27.99, 4:33.99, 5:41.99},
        10800: {1:20.99, 2:25.99, 6:29.99, 4:35.99, 5:43.99}
      }
   },
   {
    "assigments": ["Powerpoint Presentation"],
    "urgencies": URGENCY_11_DAYS,
    "levels": LEVELS5_HCUMP,
    "prices": {
        950400: {1:5.99, 2:7.99, 3:8.99, 4:10.99, 5:13.99},
        604800: {1:6.99, 2:8.99, 3:9.99, 4:11.99, 5:14.99},
        345600: {1:7.99, 2:9.99, 3:10.99, 4:12.99, 5:16.99},
        259200: {1:8.99, 2:10.99, 3:11.99, 4:14.99, 5:17.99},
        172800: {1:9.99, 2:11.99, 3:12.99, 4:15.99, 5:20.99},
        86400: {1:10.99, 2:12.99, 3:13.99, 4:16.99, 5:23.99},
        28800: {1:12.99, 2:15.99, 3:18.99, 4:22.99, 5:0}
      }
  }
]

TASK_STATUSES_DICT = dict(TASK_STATUSES)
URGENCY_DICT = dict(URGENCY)
SPACING_DICT = dict(SPACING)
STYLES_DICT = dict(STYLES)
LEVELS_DICT = dict(LEVELS)
ASSIGMENTS_DICT = dict(ASSIGMENTS)
DISCIPLINES_DICT = dict(DISCIPLINES)
COUNTRIES_DICT = dict(COUNTRIES)

# If task has public access then it will be visible to everyone.
# private tasks are visible only for users from private group.
PUBLIC_ACCESS = '0'
PRIVATE_ACCESS = '1'
ACCESS_LEVELS = ((PRIVATE_ACCESS, 'Private'),
                 (PUBLIC_ACCESS, 'Public'))
ACCESS_LEVELS_DICT = dict(ACCESS_LEVELS)

# Available ratings for a comments.
COMMENT_RATINGS = ((0, 'NULL'),
                   (1, 'ONE'),
				   (2, 'TWO'),
				   (3, 'THREE'),
                   (4, 'FOUR'),
				   (5, 'FIVE'))

# Deadline time for writers in percents.
WRITER_DEADLINE_PERCENT = 0.8

# Messages with that level of visibility are accessible to admins and editors.
MSGS_ADM = 0
# Messages with that level of visibility are accessible to writers that locked a task.
MSGS_WRITER = 1
# Messages with that level of visibility are available to customers.
MSGS_CUSTOMER = 2 

MSGS_VISIBILITY_DICT = {
  0: 'Admins&Editors',
  1: 'Writers',
  2: 'Customers'
}

# Category related item types.
# Task means task itself
TYPE_TASK = 1
# History means finished task
TYPE_HISTORY = 2

TASK_TYPES = (
  (TYPE_TASK, 'TASK'),
  (TYPE_HISTORY, 'HISTORY'))


# Check mobile constants.
reg_b = re.compile(r'android.+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|'\
                   'fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|meego.+mobile|'\
                   'midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|'\
                   'pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|'\
                   'windows (ce|phone)|xda|xiino', re.I|re.M)
reg_v = re.compile(r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|'\
                   'ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|'\
                   'au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|'\
                   'bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|'\
                   'da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|'\
                   'em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|'\
                   'gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|'\
                   'hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|'\
                   'i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|'\
                   'iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|'\
                   'le(no|xi)|lg( g|\\/(k|l|u)|50|54|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|'\
                   'ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|'\
                   'mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|'\
                   'n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|'\
                   'nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|'\
                   '\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|'\
                   'qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|'\
                   's55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|'\
                   'sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|'\
                   'sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|'\
                   'tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|'\
                   'v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|'\
                   'w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\\-|your|zeto|zte\\-', re.I|re.M)
