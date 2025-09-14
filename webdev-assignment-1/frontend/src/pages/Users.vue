<script setup>
import { ref, onMounted } from "vue";

const users = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await fetch("/api/users/");
    users.value = await res.json();
  } catch (err) {
    console.error("Failed to fetch users:", err);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <main class="container">
    <h1>👥 User List</h1>

    <p v-if="loading">Loading...</p>

    <table v-else>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.name }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>

<style>
.container {
  font-family: system-ui, sans-serif;
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
}

h1 {
  color: #111827;
  margin-bottom: 1rem;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

th, td {
  border: 1px solid #e5e7eb;
  padding: 0.5rem;
  text-align: left;
}

th {
  background: #f3f4f6;
}
</style>
