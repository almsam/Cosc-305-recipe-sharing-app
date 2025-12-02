# Cosc 305 P10 - Audit Report:

### Samira Almuallim, 62197256, 2025 WT1

## A. Introduction

This audit evaluates the progress, accuracy, and project management practices of the FitBuddy development team during Milestone 1. The main questions addressed are:

1. How accurately the team followed its charter, timeline, and Gantt chart;
2. Whether the delivered features match the video and milestone claims;
3. How effectively the team tracked risks, issues, changes, and quality metrics;
4. Whether the project is on a viable path toward its final deliverables.

When I audited the FitBuddy project, I examined documentation, milestone outputs, the demo video, and the team’s responses in the live audit meeting last Friday. This report is organized consistently across all sections: project overview, audit methodology, findings, recommendations, & conclusion

---

## B. Project Audit

### i. Project Introduction

**Project Audited:** FitBuddy – Full-Stack Fitness Application
**Team:** L04 Alloc
**Auditor:** *Samira*

FitBuddy is a fitness companion app built with React, JavaScript (Express), & a PostgreSQL backend. It provides user authentication, dashboards for members/trainers, workout and session logging, and an early Gym Finder feature. The milestone report shows 19 deliverables, with 17 passed and 2 marked Conditional Pass (likely in progress at the time of the Audit, should be full pass as of dec 5).

### ii. Audit Process and Methodology

To conduct the audit, the following materials were reviewed:

* **Milestone Review PDF** (architecture, Gantt baseline, scope changes, deliverable status, risks n issues)
* **Demo Video** (UI flows, feature completeness vs. milestone claims)
* **GitHub Repo** (only dev branch code)
* **Smartsheet exports** (change logs, risks, issues, workload trends)

#### Audit Meeting Details:

* Attendees: FitBuddy team members & I
* Purpose: Ask interview questions. Clarify discrepancies in timeline, charter objectives, dataset changes, and feature differences between the milestone video and current build.

#### Key Meeting Questions Asked:

1. How closely the team followed the Gantt chart
2. Number and reasons for timeline changes
3. Charter objectives currently at risk
4. Any missing or unimplemented quality metrics
5. Differences between video features and the current implementation

These questions were used for validating the milestone review accuracy and assessing project management practices.


---


## C. Findings

### 1a. Charter & Timeline Accuracy

**Score: 6/10**
The team initially intended to start with backend tasks but shifted earlier toward frontend work, forcing multiple timeline changes. This reduced alignment with the charter and baseline Gantt plan - but it aligned well enough after simple restructuring (at a glance)

### 1b. Video vs. Current Implementation

**Score: 7/10**
The current application includes improvements (ie a more detailed metrics page with cardio sect). UI/UX quality surpassed what the video preview suggested, but some flows appeared slightly different due to scope changes

### 1c. Milestone Review Accuracy

**Score: 8/10**
The milestone review accurately reflected deliverable statuses at a glance. The two Conditional Pass items (database setup and Docker environment) match the technical gaps seen during code review. Once again this does seem like an issue that should be solved by dec 5 however.

### 2a, 2b, & 2c. Change, Risk, and Quality Tracking

* **Change log detail: 8/10** – Comprehensive and up to date.
* **Risk & change tracking: 9/10** – Risks were well documented, and mitigations were clear.
* **Quality tracking: ~8/10** – Team members were consistent, noting that quality metrics existed but some (e.g., dataset coverage, test completeness) were not fully implemented.

### Charter Objectives at Risk

The gym dataset is smaller than originally planned (5 or 6 gyms), though more detailed. This partially worsened the "gym discovery" feature quality, but did not jeopardize quality overall

### 3. Responsiveness to Stakeholder Requests

**Score: 10/10**
The team adapted extremely well overall to stakeholder needs, especially with the added Gym Finder MVP & refined dashboard UX. The only room for improvement I saw would have been achieving this in better accordance with the plan

---

## D. Suggestions & Recommendations

1. **Stabilize the timeline earlier**
   Reduce mid-milestone deliverable movement by re thinking your 'backend first' sequence
2. **Expand quality metrics**
   Implement missing testing and data-quality metrics earlier in the milestone - room for improvement in quality tracking generally
3. **Improve dataset planning**
   The smaller but more detailed dataset works, but future milestones should document dataset trade-offs proactively
4. **Strengthen CI/CD and documentation**
   The Docker environment was functional but incomplete; onboarding documentation should ideally have been finished such that I could run the app more easily

---
