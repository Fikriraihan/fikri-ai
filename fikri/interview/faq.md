# 📄 Interview FAQ

This document contains frequently asked interview questions and answers written in my own voice, based on my personal experience as a Frontend Developer.

---

## ✅ Technical Interview FAQ

### 1. How do you implement authentication in a React app?

In my case, I'm using Supabase for authentication because of its simplicity. I implement authentication using its built-in functions. For safety, I store access tokens in `localforage` with a short expiry, and refresh tokens in cookies with longer expiry. Supabase provides built-in methods to validate if a user is authenticated, so I can use those for protected routes. If I want to handle it manually, I store tokens in cookies and create route guards to check authentication status.

### 2. How do you manage global state in your applications?

I use Zustand because it's lightweight, easy to configure, and doesn’t require boilerplate like Redux. I use it to manage filters, UI themes, and authentication states. If the state is local to a specific component tree, I prefer using React Context to avoid props drilling and keep dependencies minimal.

### 3. Tell me about a time when you had to learn a new tool quickly.

In one of my recent projects, the Sales Panel, I had to work with Mantine UI even though I wasn’t familiar with it at first. Since the project was already in progress, I needed to adapt quickly. I started by reading the documentation, then watching tutorials to see how other developers use it in real projects. Once I got the hang of it, I started implementing it in isolated components before using it in the actual project. That approach helped me speed up my learning and stay productive during development.

### 4. How do you handle tight deadlines?

Sure, thats a very good question and this is very related to my current situation. When im facing a tight deadlines, the first thing that i did is break down the tasks into smaller, organized, and manageable tasks. After that i set the priority of each tasks based on the urgency and impact to the project. Then we communicated regulary to make sure alignment because this is very important, also set transparency about the progress and problems if there is. At the end, we can deliver all the tasks on time even before the deadline or the end of the sprint. this experience taught that if we can manage our tasks, it really increases the efficiency of the development, also communication is the key to most of problems. and of course maintain high discipline

### 5. How do you optimize performance in a React application?

For performance, I apply memoization using `React.memo` and `useMemo`, lazy loading with dynamic imports, and virtualization when rendering large lists (e.g. with `react-window`). I also make sure the global state is scoped properly to prevent unnecessary re-renders, and keep an eye on bundle size by splitting code when needed.

### 6. What’s your approach to responsive design?

I use Tailwind CSS, which makes responsive design easy with mobile-first utility classes. I use its responsive breakpoints to adjust layout across screen sizes and rely on CSS Flexbox and Grid for structure. I usually test on browser dev tools and tools like Responsively App to ensure the layout works well everywhere.

### 7. How do you integrate APIs and handle errors?

I usually use `react-query` (or `@tanstack/react-query`) for API integration. It gives me caching, retries, and loading/error state management out of the box. I wrap my API functions with try/catch blocks, show toast alerts for user feedback, and log errors for debugging. If needed, I integrate tools like Sentry for error tracking.

### 8. How do you handle form validation in React?

I usually use `react-hook-form` because of its minimal re-renders and ease of integration with schema validation libraries like `zod`. For example, in the PU & Budgeting System project, I used react-hook-form with `zod` to handle validation for login and submission forms. This setup allowed me to define clear validation rules and display helpful feedback to users instantly.

By combining react-hook-form with `zod`, I could keep my form logic declarative and maintainable, while also ensuring robust validation both on the frontend and when preparing data for backend APIs.

### 9. Have you used testing frameworks?

Yes, I’ve started using Jest and React Testing Library for testing. I’m comfortable writing basic unit tests and rendering tests, and I'm still learning about integration testing and mocking API responses.

### 10. How do you collaborate with backend or design teams?

I make sure to align early with backend engineers using tools like Swagger or Postman to clarify API requirements. For design, I use Figma and pay attention to consistency in spacing, typography, and layout. I ask questions early if something’s unclear to avoid rework and always keep the communication open.

### 11. Have you worked with animations or micro-interactions in your UI?

Yes, I've worked with both Framer Motion and GSAP in several of my personal projects, including my portfolio. I'm quite confident using them for animations and transitions. While I haven't had the chance to use them in real-world company projects yet—mainly because the teams I worked with didn’t require animation-heavy interfaces—I’m very comfortable implementing motion in production-ready code if the need arises.

### 12. Can you explain a system you’ve worked on end-to-end?

One of the most complete systems I’ve worked on recently is called PU & Budgeting at my current company. It's a platform where employees can submit requests for goods or services, and the request goes through a full approval and purchasing workflow.

Here’s the typical process:

1. A user submits a request for goods or services.
2. The request is approved by the user’s department head.
3. If needed, additional relevant department heads review the request.
4. The purchasing team reviews it and offers vendor options with pricing.
5. The user selects an offering.
6. The system generates an SPBDJ document summarizing the request.
7. Final approval is given by the division head.
8. A purchase order (PO) is created.

I work on the frontend side using React (with Vite), Zustand, Tailwind CSS, React Query, React Hook Form, and ShadCN. I also collaborate in API discussions and help define how the flow should work. The main challenges in this project are building dynamic forms, handling a multi-step approval process, and rendering different UIs based on user roles. It's a complex but rewarding system to work on.

### 13. Have you worked on AI or automation features?

Yes, I’ve been actively exploring AI and automation. I built a ChatGPT-style interface clone and published it on GitHub. I’ve also created automation workflows using n8n—such as automating email flows, connecting form submissions to Airtable or Google Sheets, and using Deep Research APIs. One of the most exciting projects I’ve worked on is building a RAG-based chatbot using LangChain, Pinecone for vector search, and OpenAI for completions. I used Gradio to create a lightweight UI so the chatbot could respond in real time. These experiments helped me understand how to build end-to-end AI features into practical interfaces.

### 14. What are your goals as a developer?

In the short term, I want to work remotely for companies abroad, especially in the fields of AI, automation, and animation — because I truly enjoy solving problems in those areas. Long term, my goal is to become an independent developer, building my own products and leaving the traditional 9-to-5 cycle behind. I’m passionate about projects that are both technically challenging and creatively fulfilling.

---

_End of Interview FAQ section._
