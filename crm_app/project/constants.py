from enum import Enum


class Project(Enum):
    SKILLZ = 'Skillz'
    MATIFIC = '10 אצבעות (Matific)'
    PLETHORA = 'plethora'
    ICODE = 'icode'
    ACCELIUM = 'accelium'
    ROBOTICS = 'רובוטיקה'
    OTHER = 'אחר'


class Client(Enum):
    TEACHER = 'מורה'
    PARENT = 'הורה'
    DIRECTOR = 'מנהל'
    STUDENT = 'תלמיד'


class Problem(Enum):
    OTHER = 'אחר'
    SLOW = 'איטיות'
    CONNECTION = 'בעית התחברות'
    START = 'הרצת סבב'
    AUTH = 'הרשאה לרכז רשום'
    ENTRY = 'כניסה לתחרות'
    NEXTLEVEL = 'לא עובר לשלב הבא'
    RESULT = 'לוח תוצאות'
    SYSTEM = 'מערכת לא עובדת'
    REGISTR = 'רישום'
    QCODE = 'שאלה בקוד'
    QGAME = 'שאלה בתוך המשחק'
    SALES = 'שיווק'
    LANG = 'שפות'


class Status(Enum):
    NEW = 'פנייה חדשה'
    INPROCESS = 'בטיפול'
    FINISHED = 'טופל'


class Service(Enum):
    SKILLZ = 'Skillz'
    MATIFIC = 'Matific'
    PLETHORA = 'plethora'
    ICODE = 'icode'
    ACCELIUM = 'accelium'
    ROBOTICS = 'רובוטיקה'
    PORTAL = 'אחר'