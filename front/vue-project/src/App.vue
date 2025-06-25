<script setup>
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'
</script>


<script>
import { ref } from 'vue'

const cursorPosition = ref(null)

const handleButtonClick = (event) => {
  cursorPosition.value = {
    x: event.clientX,
    y: event.clientY,
  }
}

function changePosition() {
  setTimeout(() => {

    axios.get('http://127.0.0.1:8000/getPosition')
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('Ошибка при выполнении GET-запроса:', error);
      });

  }, 1000)
}


</script>


<template>
  <header>
    <h1 class="hello">Добро пожаловать в TEXT RECOGNITION!</h1>

    <div class="underHead">
      <h2>Ниже будет форма с распозднаным и переведенным текстом</h2>
    </div>

    <div class="boxes">
      <div class="recognitionBox">
        <h3>Здесь будет распозднанный текст</h3>
      </div>

      <div class="translateBox">
        <h3>Здесь будет перевод</h3>
      </div>
    </div>

    <div class="buttons">
      <div class="container">
        <button @click="handleButtonClick">Нажми, чтобы узнать положение курсора</button>
        <div v-if="cursorPosition" class="position-display">
          Координаты курсора: X: {{ cursorPosition.x }}, Y: {{ cursorPosition.y }}
        </div>
      </div>

      <div class="changePosition">
        <button @click="changePosition">Изменить положения рамки</button>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  text-align: center;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  gap: 20px;
}

button {
  padding: 12px 24px;
  font-size: 16px;
  cursor: pointer;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #33a06f;
}

.position-display {
  padding: 12px;
  background-color: #f5f5f5;
  border-radius: 4px;
  font-family: monospace;
}
</style>
