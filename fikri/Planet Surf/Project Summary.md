# 🏢 PT Planet Selancar Mandiri (Planet Surf)

- **Role:** Front-End Developer
- **Period:** Aug 2024 – Present
- **Tech Stack:** React.js · Vite · TypeScript · JavaScript · Tailwind CSS · Zustand

---

## 🧐 Summary

Contributed to the development of three key internal platforms used by Area Managers, Operations, and Management Teams:

- **OTB Forecasting Platform**
- **Sales Panel Dashboard**
- **PU & Budgeting System**

---

## 📁 Project: OTB Forecasting Platform

- **Tech Stack:** React.js · Vite · Zustand · Tailwind CSS · React Query · Mantine
- **Company:** Planet Surf

An interactive dashboard that allows the OTB team to forecast inventory based on historical data. Users can upload Excel files, filter information, and view analyzed output in real-time.

### 🔧 Key Contributions

- Built modern UI/UX using React, Tailwind CSS, Zustand, and TypeScript.
- Implemented core features including:

  - File upload with validation (Excel)
  - Dynamic and multi-level filtering
  - Table view with zoom, pagination, and infinite scroll
  - Data export to Excel

### 📄 PRD Highlights

**Objective:**
To allow the OTB team to estimate inventory based on past data through intuitive data upload and filtering interfaces.

**User Roles & Access:**

| Role              | Access Level               |
| ----------------- | -------------------------- |
| Area Support Team | Update Target Ending Stock |
| Analyst Team      | Analyze and view forecasts |
| OTB & Ops Team    | Full platform access       |

**Key Features:**

1. Table and List Views with zoom functionality
2. Infinite Scroll and Pagination toggle
3. Upload Return, Target, and Closing Stock data
4. Advanced multi-filtering

**Functional Requirements:**

- Switchable table/list views
- Auto-categorized uploads into PD1, PD2, PD3
- Fast, responsive filtering

**Non-Functional Requirements:**

- Load time under 30s with large datasets
- Intuitive multi-user UX
- Role-based data access and security

**Milestones:**

- **Phase 1 (Jul 15):** IHB data display, authentication, upload, table & filtering
- **Phase 2 (Jul 19):** PD1/PD2/PD3 reports, parameter integration
- **Phase 3 (Oct 25):** UI redesign, performance optimization, front-end improvements (led by me)

**Success Metrics:**

- 90% faster load time
- Reduced manual tasks via automation
- High scalability & secure access control

---

## 📁 Project: Sales Panel Dashboard

- **Tech Stack:** React.js · Vite · Zustand · Tailwind CSS · React Query · React Hook Form · ShadCN UI
- **Company:** Planet Surf

A real-time dashboard designed for Area Managers and Store Heads to track sales performance by store, brand, and staff.

### 🔧 Key Contributions

- Designed a responsive dashboard viewable across mobile and desktop
- Developed data filtering by date, role, and region
- Enabled secure downloads in PDF, Excel, and CSV format
- Implemented role-based access to restrict data by user level

### 📄 PRD Highlights

**Pain Points & Solutions:**

- **Limited visibility:** introduced role-based performance insights
- **Manual reporting:** centralized automated reporting

**Features:**

1. Real-time Dashboard Insights
2. Custom date filters
3. Export options for reports

**Functional Requirements:**

- Visualization of sales metrics: revenue, target, achievement
- Real-time data sync
- Export to PDF, Excel, CSV
- Role-specific views for AM, SSH, and Ops

**Non-Functional Requirements:**

- Load time under 3s
- Cross-device compatibility
- Role-based encryption and access

**Version Releases:**

- **v1.0:** Dashboard, Brand, Store, Staff insights
- **v1.1:** Staff contribution tracking, search dropdown
- **v1.2:** Dark mode, responsive fixes, UI upgrades

**Success Metrics:**

- 70% user adoption within 1 month
- 98% data accuracy (cross-validated with iReap)
- Monthly report generation by all users

---

## 📁 Project: PU & Budgeting System

- **Tech Stack:** React.js · Vite · Zustand · Tailwind CSS · React Query · React Hook Form · ShadCN UI · Storybook
- **Company:** Planet Surf

An internal system for managing requests and approvals for goods or services, involving multiple roles and dynamic approvals.

### 🔧 Key Contributions

- Developed the frontend using React (Vite), Zustand, Tailwind CSS, React Query, React Hook Form, and ShadCN
- Helped define workflow logic and API structure with the team
- Built dynamic multi-step forms and approval interface with role-based rendering

### ✅ Workflow Steps

1. User submits a request for goods/services
2. Approval by the user's department head
3. Optional approval by relevant additional department heads
4. Purchasing team provides vendor offering with price options
5. User selects an offering
6. System generates SPBDJ document summarizing request
7. Final approval from division head
8. PO (Purchase Order) creation

### ⚡ Key Features

- Dynamic form rendering based on request type and user role
- Multi-role approval flow UI
- File/document submission and review
- SPBDJ generator

### ⚖️ Challenges

- Adapting UI across varied roles
- Flexible form structure
- Approval logic across multiple levels

---
