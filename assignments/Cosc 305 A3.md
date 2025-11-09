# Cosc 305 Assignment 3:
### Samira Almuallim, 62197256, 2025 WT1

---

# Q1:

### 1. A:

All paths:
ABCF, 2+4+3+3=12 days
ADF, 2+7+3=12 days
AEF, 2+8+3=13 days

AEF is the critical paths

### 1. B & C:

| Task | Task precedence | Length (days) | ES | EF | LS | LF | Slack (LS−ES) |
| ---- | --------------- | ------------- | -- | -- | -- | -- | -------------- |
| A    | _ (start)       | 2             | 0  | 2  | 0  | 2  | 0              |
| B    | A - B           | 4             | 2  | 6  | 3  | 7  | 1              |
| C    | B - C           | 3             | 6  | 9  | 7  | 10 | 1              |
| D    | A - D           | 7             | 2  | 9  | 3  | 10 | 1              |
| E    | A - E           | 8             | 2  | 10 | 2  | 10 | 0              |
| F    | C, D, E - F     | 3             | 10 | 13 | 10 | 13 | 0              |

Total Slack = LS − ES = LF − EF

SA =  0-0  = 0
SB =  3-2  = 1
SC =  7-6  = 1
SD =  3-2  = 1
SE =  2-2  = 0
SF = 10-10 = 0

### 1. D:

| Activity | Team member | Day of the week |
| - | ---------------------------- | -------------------------- |

|             |       | M | T | W | Th | F | Sa | S | M | T | W | Th | F | Sa | S | M | T | W | Th |  |
| ----------- | ----- | - | - | - | -- | - | -- | - | - | - | - | -- | - | -- | - | - | - | - | -- | - |
| **A** | Jill  | X | X |   |    |   |    |   |   |   |   |    |   |    |   |   |   |   |    |  |
| **B** | Tom   |   |   | X | X  | X | __ | _ | X |   |   |    |   |    |   |   |   |   |    |  |
| **C** | Jill  |   |   |   |    |   |    |   |   | X | X | X  |   |    |   |   |   |   |    |  |
| **D** | Sam   |   |   | X | X  | X | __ | _ | X | X | X | X  |   |    |   |   |   |   |    |  |
| **E** | Susan |   |   | X | X  | X | __ | _ | X | X | X | X  | X |    |   |   |   |   |    |  |
| **F** | Ken   |   |   |   |    |   |    |   |   |   |   |    |   |    |   | X | X | X |    |  |

### 1. E:

No - since Tom doesn't start until Jill went on break, & Jill didn't resume until tom finished. In addition, kens work could also be picked up by susan or sam as no overlap exists

So Jill, Tom, & Ken's work can all be mixed into 1 persons workload -- thus only 3 of the 6 are needed

### 1. F:

| Activity | Team member | Day of the week                                                                |
| - | ---------------------------- | -------------------------- |

|                |       | M | T | W | Th | F | Sa | S | M | T | W | Th | F | Sa | S | M | T | W | Th |  |
| -------------- | ----- | - | - | - | -- | - | -- | - | - | - | - | -- | - | -- | - | - | - | - | -- | - |
| **ABCF** | Tom   | A | A | B | B  | B | __ | _ | B | C | C | C  |   |    |   |   |   |   |    |  |
| **D**    | Sam   |   |   | D | D  | D | __ | _ | D | D | D | D  |   |    |   |   |   |   |    |  |
| **E**    | Susan |   |   | E | E  | E | __ | _ | E | E | E | E  | E | __ | _ | F | F | F |    |  |

I would merge Jill & Tom's work, as well as giving Ken's work to Susan

### 1. G:

| Activity | Team member | Day of the week                                                                |
| - | ---------------------------- | -------------------------- |

|                |       | M | T | W | Th | F | Sa | S | M | T | W | Th | F | Sa | S | M | T | W | Th |  |
| -------------- | ----- | - | - | - | -- | - | -- | - | - | - | - | -- | - | -- | - | - | - | - | -- | - |
| **ABCF** | Tom   | A | A | B | B  | B | __ | _ | B | C | C | C  |   |    |   |   |   |   |    |  |
| **D**    | Sam   |   |   | D | D  | D | __ | _ | D | D | D | D  |   |    |   |   |   |   |    |  |
| **E**    | Susan |   |   | E | E  | E | __ | _ | E | E | E | E  | E | __ | _ | F | F | F |    |  |

Because of my specific solution to F, it would look the same as Tom can single handedly clear both Their & Jill's work

### 1. H:

The critical pth is AEF at 13 days, so the only tasks that could reduce the length of the project are A, E, or F

thus the candidates are: A for 1000$, E for 1200$, or F for 1800$

Therefore: I choose task A, as it will reduce the schedule by a day (unlike B C or D) & costs less then E or F for the same 1 day benefit

---

# Q2:

### 2. A:

pert formula: t_e = (t_o+4t_m+t_p)/6

| Task |   expected time:          |  variance:                 |
| - | ---------------------------- | -------------------------- |

|   | (t_e=(t_o+4t_m+t_p)/6)          | (\sigma^2=((t_p-t_o)/6)^2)        |
| - | ------------------------------- | --------------------------------- |
| A | (1 + 4·2 + 3)/6 =**2**   | ((3−1)/6)^2 =**0.111111**  |
| B | (2 + 4·4 + 6)/6 =**4**   | ((6−2)/6)^2 =**0.444444**  |
| C | (1 + 4·3 + 5)/6 =**3**   | ((5−1)/6)^2 =**0.444444**  |
| D | (6 + 4·7 +14)/6 =**8**   | ((14−6)/6)^2 =**1.777778** |
| E | (5 + 4·8 +11)/6 =**8**   | ((11−5)/6)^2 =**1.000000** |
| F | (1 + 4·3 + 8)/6 =**3.5** | ((8−1)/6)^2 =**1.361111**  |

Expected duration, variance, & SD:

ABCF - 2+4+3+3.5 = 12.5 days
   var - 0.111111 + 0.444444 + 0.444444 + 1.361111 = 1.803
   sd = sqrt(var) = 1.537
ADF  - 2+8+3.5 = 13.5 days
   var - 0.111111 + 1.777778 + 1.361111 = 3.250000
   sd = sqrt(var) = 1.803
AEF  - 2+8+3.5 = 13.5 days
   var - 0.111111 + 1.000000 + 1.361111 = 2.472222
   sd = sqrt(var) = 1.572

### 2. B:

| Path | optimistic scenario                          |
| ---- | ------------------------------------------- |
| ABCF | A(1) + B(2) + C(1) + F(1) =**5** days |
| ADF  | A(1) + D(6) + F(1) =**8** days        |
| AEF  | A(1) + E(5) + F(1) =**7** days        |

optimistic total time = max([5, 8, 7]) = 8 days

SD = SD(ADF) = 1.8 days   //see 2A

### 2. C:

| Path | pessimistic scenario                         |
| ---- | -------------------------------------------- |
| ABCF | A(3) + B(6) + C(5) + F(8) =**22** days |
| ADF  | A(3) + D(14) + F(8) =**25** days       |
| AEF  | A(3) + E(11) + F(8) =**22** days       |

pessimistic total time = max([22, 25, 22]) = 25 days

SD = SD(ADF) = 4 days  //see 2A

### 2. D:

I. Probability to complete the project in 18 days

Z-score: Z = X-u / sd = 18-13.67 / 1.8 = 4.33 / 1.8 ~= 2.41

Z 2.41 - 99.2% chance of completing the project in under 18 days

II. Probability to complete the project in 12 days

Z-score: Z = X-u / sd = 12-13.67 / 1.8 = 1.67 / 1.8 ~= 0.93

Z 0.93 - 17.62% chance of completing the project in under 12 days
