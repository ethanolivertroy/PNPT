
# SQL Injection Attacks

- https://www.owasp.org/index.php/Top_10-2017_A1-Injection


## Blind SQL Injection


## SQL Injection Defenses

### Defense 1: Parameterized Statements
-   ﻿﻿Ensure inputs (parameters) are used safely in SQL statements
-   ﻿﻿Example: "SELECT * FROM users WHERE email =?";
-   ﻿﻿Example: "SELECT * FROM users WHERE email = ''' + email + "";

### Defense 2: Sanitizing Input