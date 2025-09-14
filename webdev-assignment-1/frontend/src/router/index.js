import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/pages/Home.vue";
import Users from "@/pages/Users.vue";


const routes = [
  { path: "/", component: Home },
  { path: "/users", component: Users },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
