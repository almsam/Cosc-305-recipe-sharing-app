# Cosc 305 Assignment 3:

### Samira Almuallim, 62197256, 2025 WT1

## Q1:

### Given table (interpreted)

| Activity | Pre req | Normal time (days) | Crash time (days) | Normal cost | Crash cost |
| -------- | ------- | ------------------ | ----------------- | ----------- | ---------- |
|        A |   –     |                  2 |                 1 |      $1,200 |     $1,600 |
|        B |   A     |                  5 |                 1 |      $1,500 |     $4,500 |
|        C |   B     |                  2 |                 2 |        $750 |       $750 |
|        D |   A     |                  5 |                 3 |      $2,500 |     $3,500 |
|        E |   A     |                  6 |                 4 |      $3,000 |     $4,000 |
|        F | C,D,E   |                  5 |                 3 |      $2,000 |     $3,000 |

Normal path lengths:

* A–B–C–F = 2+5+2+5 = **14** days (crit path)
* A–D–F = 2+5+5 = 12 days
* A–E–F = 2+6+5 = 13 days

---

## (a) Cost to complete in **14 days** (normal schedule)


Sum of normal costs:
\[
1200+1500+750+2500+3000+2000 = 10,950
\]

**Answer (a): $10,950**

---

## (b) Crash cost per time period (per day):

Compute \[((\text{CrashCost} - \text{NormalCost})/(\text{NormalTime} - \text{CrashTime})):\]

* A: \[((1600-1200)/(2-1)=400/1=400/\text{day})\]
* B: \[((4500-1500)/(5-1)=3000/4=750/\text{day})\]
* C: \[//not Possible As 750=750\]
* D: \[((3500-2500)/(5-3)=1000/2=500/\text{day})\]
* E: \[((4000-3000)/(6-4)=1000/2=500/\text{day})\]
* F: \[((3000-2000)/(5-3)=1000/2=500/\text{day})\]

**Ans (b):** A $400/day; B $750/day; C N/A; D $500/day; E $500/day; F $500/day.

---

## (c) Crash to complete in **8 days** (minimum-cost crash schedule)

**Obj:** reduce project duration from 14  ->  8 (need 6 days reduction).

**Available crash capacity on initial critical path A–B–C–F:**

* A: can reduce by 1 day (2 -> 1)
* B: can reduce by 4 days (5 -> 1)
* C: cannot reduce (2 -> 2)
* F: can reduce 2 days (5 -> 3)
  Total possible reduction on that path = 1+4+0+2 = **7 days** (>= 6 required) -> Thus this is viable

**Crash procedure (minimum incremental cost on the current critical path, recalculating critical path after each step):**

1. **Crash A by 1 day** (cheapest on current critical path at $400/day).

   * A: 2 -> 1, extra cost = $400
   * New proj length: 14  ->  13 days
   * New path lengths: A–B–C–F = 13; A–D–F =11; A–E–F = 12

2. **Crash F by 2 days** (2nd cheapest on the critical path at $500/day; F can be shortened by 2)

   * F: 5 -> 3, extra cost = 2*$500 = $1,000
   * New project length: 13  ->  11 days
   * New path length: A–B–C–F =11; A–D–F = 9; A–E–F = 10

3. **Remaining reduction we require:** 11  ->  8 = **3 days**.

   * On current critical path A–B–C–F, only B can still be crashed (C cannot) B’s crash cost = $750/day
   * Crash **B by 3 days**: B: 5 -> 2, extra cost = 3 * $750 = $2,250
   * After this: A–B–C–F = 1 + 2 + 2 + 3 = **8 days**  ->  target reached.

I didn't crash D or E because they re not on the critical path and crashing them would not reduce the proj duration until crit path changed, my chosen sequence minimizes incremental cost at each step

**Activities shortened:** A by 1 day, F by 2 days, B by 3 days

---

## (d) Total proj cost when completed in **8 days**

Start from normal cost $10,950 (from (a)). Add incremental crash costs:

* A: +$400 (1 day)  ->  A cost becomes $1,600 (which equals given crash cost)
* F: +$1,000 (2 days)  ->  F cost becomes $3,000 (full crash cost)
* B: +$2,250 (3 days)  ->  B cost becomes $1,500 + $2,250 = $3,750

Sum extra crash cost = $400 + $1,000 + $2,250 = $3,650

Total project cost = normal cost + crash increments = $10,950 + $3,650 = **$14,600**

**Ans (d): $14,600**

---

## Q2:



### Given

* Planned Value (PV) = $28,000
* Earned Value (EV) = $25,000
* Actual Cost (AC) = $29,500

## (a) Budget status - Over or under budget?

**Cost Variance (CV)** = EV − AC = $25,000 − $29,500 = **−$4,500** - negative CV means **over budget** to date

**Cost Performance Index (CPI)** = EV / AC = 25,000 / 29,500 = **0.8475** (~= **0.85**)
CPI < 1 ⇒ you are getting $0.85 value for every $1 spent - **cost efficiency is poor**

**Interpretation:** the phase is currently **over budget** by $4,500 and performing at ~85% cost efficiency - spending must go down!

---

## (b) Schedule status - On time or behind?

**Schedule Variance (SV)** = EV − PV = $25,000 − $28,000 = **−$3,000** - negative SV means **behind schedule** (in value terms)

**Schedule Performance Index (SPI)** = EV / PV = 25,000 / 28,000 = **0.8929** (~= **0.89**)
SPI < 1 ==> about **89%** of planned work value has been earned → **behind schedule**

**Interpretation:** the phase is **behind schedule** (shortfall $3,000 in earned value)

---

## (c) Quick forecast (optional) - estimate to complete the phase

You need the **Budget at Completion (BAC)** to make a formal EAC. If the phase BAC = the planned value to date (PV = $28,000) then:

One common EAC formula:
**EAC = BAC / CPI** ==> EAC ~= 28,000 / 0.8475 ~= **$33,050**

Alternate form: **EAC = AC + (BAC − EV)/CPI** ==> 29,500 + (28,000−25,000)/0.8475 ~= 29,500 + 3,539 ~= **$33,039** (same within rounding)

**Implication:** if trends continue & BAC = $28k, expected final cost ~= **$33k** - **~$5k over original BAC**

(If BAC =/= PV, substitute actual BAC into the same formulas.)

---

## (d) Actionable implications (brief)

* **Over budget** and **behind schedule** - both warning signs
* Performance indices CPI ~= 0.85 and SPI ~= 0.89 indicate corrective action needed (cost control, scope/replanning, re-allocation of resources, staff changes, etc etc)
* Produce an **EAC** using the true BAC, re-evaluate remaining work, and prepare a remedial plan (cost reductions, replanning, prioritized or narrow er scope)
* Re assess assumptions, risks, and approvals (license/gaming items may be driving rework/costs).

---

### Common formulas for Q 34567

* **SV (Schedule Variance)** = EV − PV
* **CV (Cost Variance)** = EV − AC
* **SPI (Schedule Performance Index)** = EV / PV
* **CPI (Cost Performance Index)** = EV / AC

---

## Q3:

PV = $190,000, EV = $150,000, AC = $170,000

**(a)**
SV = EV − PV = $150,000 − $190,000 = **−$40,000**
CV = EV − AC = $150,000 − $170,000 = **−$20,000**

**(b)** Conclusion:

* **Behind schedule** (SV < 0)
* **Over budget / cost overrun** (CV < 0).

---

## Q4:

//(same values) PV = $190,000, EV = $150,000, AC = $170,000

**(a)**
SPI = EV / PV = 150,000 / 190,000 = **0.7895** (rounded)

**(b)**
CPI = EV / AC = 150,000 / 170,000 = **0.8824** (rounded)

**(c)** Conclusion:

* **SPI < 1 (0.7895)** - project is **behind schedule** (only ~78.95% of planned work earned)
* **CPI < 1 (0.8824)** - proj is **cost-inefficient / over budget** (you get  ~=$0.88 value per $1 spent)

---

## Q5

PV = $140,000, EV = $160,000, AC = $145,000

**(a)**
SV = EV − PV = $160,000 − $140,000 = **+$20,000**

**(b)**
CV = EV − AC = $160,000 − $145,000 = **+$15,000**

**(c)** Conclusion:

* **Ahead of schedule** (SV > 0)
* **Under budget / cost favorable** (CV > 0)

---

## Q6

(same values) PV = $140,000, EV = $160,000, AC = $145,000

**(a)**
SPI = EV / PV = 160,000 / 140,000 = **1.1429** (rounded)

**(b)**
CPI = EV / AC = 160,000 / 145,000 = **1.1034** (rounded)

**(c)** Conclusion:

* **SPI > 1 (1.1429)** - project is **ahead of schedule**
* **CPI > 1 (1.1034)** - project is **cost-efficient / under budget** (~=$1.10 value per $1 spent)

---

## Q7

PV = $240,000, EV = $250,000, AC = $270,000

**(a)**
SV = EV − PV = $250,000 − $240,000 = **+$10,000**.

**(b)**
CV = EV − AC = $250,000 − $270,000 = **−$20,000**.

**(c)**
SPI = EV / PV = 250,000 / 240,000 = **1.0417** (rounded).

**(d)**
CPI = EV / AC = 250,000 / 270,000 = **0.9259** (rounded).

**(e)** Conclusion:

* **Ahead of schedule** (SPI > 1, SV > 0).
* **Over budget / cost-inefficient** (CPI < 1, CV < 0): the project is progressing faster than planned but spending is way too high - higher than the value earned

---

