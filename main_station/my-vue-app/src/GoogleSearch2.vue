<template>
    <div id="app">
      <header>
        <h1>Search Results</h1>
      </header>
      <main>
        <div class="search-box">
          <input v-model="query" type="text" placeholder="Search..." />
          <button @click="performSearch">Search</button>
        </div>
        
        <div v-if="results.length" class="results">
          <div v-for="(item, index) in results" :key="index" class="result-item">
            <h2>{{ item.title }}</h2>
            <p>{{ item.content }}</p>
            <a :href="item.commentsUrl" target="_blank">Read more</a>
          </div>
        </div>
  
        <div v-else>
          <p>No results found.</p>
        </div>
      </main>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  

  export default {
    name: 'App',
    data() {
      return {
        query: '',       // 搜索关键词
        results: []      // 存储返回的结果
      };
    },
    methods: {
      async performSearch() {
        try {
          const apiUrl = process.env.VUE_APP_API_BASE_URL || 'http://localhost:8080';
          console.log('API Base URL:', process.env.VUE_APP_API_BASE_URL);
          console.log('Current environment:', process.env.NODE_ENV);
          const response = await axios.get('${apiUrl}/search/ifeng-search-server/all/searchIndices', {
            params: { k: this.query } // 将搜索关键词传递给接口
          });
          this.results = response.data.items; // 假设接口返回的搜索结果存储在 `items` 中
          console.log('result.length: ', this.results.length)
        } catch (error) {
          console.error('Error fetching search results:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
  }
  
  #app {
    text-align: center;
    background: white;
    padding: 20px;
    margin: 20px auto;
    width: 50%;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .search-box {
    margin-bottom: 20px;
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
  
  .results {
    margin-top: 20px;
  }
  
  .result-item {
    padding: 10px;
    border-bottom: 1px solid #ccc;
    text-align: left;
  }
  
  .result-item h2 {
    margin: 0;
  }
  
  .result-item p {
    color: #555;
  }
  
  .result-item a {
    color: #4285f4;
    text-decoration: none;
  }
  </style>
  