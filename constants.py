import re

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


# Task related statuses.
RUNNING = 0
NOT_ASSIGNED = 1
FINISHED = 2
TASK_STATUSES = (
  (RUNNING, 'RUNNING'),
  (NOT_ASSIGNED, 'NOT ASSIGNED'),
  (FINISHED, 'FINISHED'))

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


DISCIPLINES = (
  ('hs', 'History'), ('ln', 'Linguistics'), ('lt', 'Literature'),
  ('pa', 'Performing arts'), ('ph', 'Philosophy'), ('rg', 'Religion'),
  ('va', 'Visual arts'), ('an', 'Anthropology'), ('ar', 'Archaeology'),
  ('as', 'Area studies'), ('cu', 'Cultural and ethnic studies'),
  ('ec', 'Economics'), ('gs', 'Gender and sexuality studies'),
  ('ge', 'Geography'), ('ps', 'Political science'), ('py', 'Psychology'),
  ('so', 'Sociology'), ('ss', 'Space sciences'),
  ('es', 'Earth sciences'), ('ls', 'Life sciences'), ('ch', 'Chemistry'))


ASSIGMENTS = (
  ('es', 'Essay'), ('re', 'Report'), ('ab', 'Abstract'),
  ('an', 'Annotated bibliography'), ('rw', 'Review'), ('cs', 'Case Study'))


LEVELS = (
  ('hs', 'High School'), ('co', 'College'), ('un', 'University'),
  ('ms', 'Master\'s'), ('ph', 'PHD'))

# Urgency is more convenient to represent as time in seconds and label
URGENCY = (
  (21600, '6hours'), (43200, '12 hours'), (86400, '1 day'), (172800, '2 days'),
  (259200, '3days'), (518400, '6days'), (1036800, '12days'),
  (2073600, '24+days'))


SPACING = ((1, 'Single'), (2, 'Double'))

STYLES = (
  (1, 'MLA'), (2, 'APA'), (3, 'Chicago'), (4, 'Turabian'), (5, 'Harvar'),
  (6, 'other'))

# If task has public access then it will be visible to everyone.
# private tasks are visible only for users from private group.
PUBLIC_ACCESS = 0
PRIVATE_ACCESS = 1
ACCESS_LEVELS = ((PUBLIC_ACCESS, 'PUBLIC ACCESS'),
                 (PRIVATE_ACCESS, 'PRIVATE ACCESS'))

# Available ratings for a comments.
COMMENT_RATINGS = ((0, 'NULL'), (1, 'ONE'), (2, 'TWO'), (3, 'THREE'),
                   (4, 'FOUR'), (5, 'FIVE'))

WRITER_GROUP = 'writer'

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
