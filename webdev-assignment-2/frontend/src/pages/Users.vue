<script setup>
import { ref, onMounted } from "vue";

const users = ref([]);
const loading = ref(true);
const newName = ref("");

const fetchUsers = async () => {
  try {
    const res = await fetch("/api/users/");
    users.value = await res.json();
  } catch (err) {
    console.error("Failed to fetch users:", err);
  } finally {
    loading.value = false;
  }
};

const addUser = async () => {
  if (!newName.value) return;

  try {
    const res = await fetch(`/api/users/?name=${encodeURIComponent(newName.value)}`, {
      method: "POST",
    });
    const user = await res.json();
    users.value.push(user);
    newName.value = "";
  } catch (err) {
    console.error("Failed to add user:", err);
  }
};

onMounted(fetchUsers);
</script>

<template>
  <main class="container">
    <h1>👥 User List</h1>

    <form @submit.prevent="addUser" class="form">
      <input v-model="newName" placeholder="Enter name" />
      <button type="submit">Add User</button>
    </form>

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

.form {
  margin-bottom: 1rem;
}

input {
  padding: 0.4rem;
  margin-right: 0.5rem;
}

button {
  padding: 0.4rem 0.8rem;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #1d4ed8;
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
