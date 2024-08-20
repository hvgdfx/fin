<template>
    <div id="app">
      <header>
        <h1>Google Search</h1>
      </header>
      <main>
        <div class="search-box">
          <input v-model="query" type="text" placeholder="Search..." />
          <button @click="performSearch">Search</button>
        </div>
      </main>
      <footer>
        <p>&copy; 2024 My Search Page</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'App',
    data() {
      return {
        query: ''
      };
    },
    methods: {
      performSearch() {
        if (this.query.trim()) {
          window.location.href = `https://www.google.com/search?q=${encodeURIComponent(this.query)}`;
        } else {
          alert('Please enter a search term.');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #f0f0f0;
  }
  
  #app {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  header {
    margin-bottom: 20px;
  }
  
  .search-box {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  input {
    width: 300px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    margin-left: 10px;
    border: none;
    background-color: #4285f4;
    color: white;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #357ae8;
  }
  
  footer {
    margin-top: 20px;
  }
  </style>
  