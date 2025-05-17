<template>
  <div id="app">
    <h1>Retro Birth Day</h1>
    <form @submit.prevent="fetchGame">
      <label for="birthdate">Enter your birth date:</label>
      <input type="date" v-model="birthdate" required />
      <button type="submit">Get Retro Game</button>
    </form>
    <div v-if="game">
      <h2>Game from your birth date:</h2>
      <p>{{ game }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      birthdate: '',
      game: null,
    };
  },
  methods: {
    async fetchGame() {
      try {
        const response = await fetch(`http://localhost:5000/api/game?date=${this.birthdate}`);
        const data = await response.json();
        this.game = data.game;
      } catch (error) {
        console.error('Error fetching game:', error);
      }
    },
  },
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
form {
  margin-bottom: 20px;
}
</style>