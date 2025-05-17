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
      <h1 v-if="game.title">{{ game.title }}</h1>
      <p v-if="game.release_date">Release Date: {{ game.release_date }}</p>
      <p v-if="game.description">Description: {{ game.description }}</p>
    </div>
    <div v-if="found == false">
      <p>No game found for this date.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      birthdate: '',
      game: null,
      found: null
    };
  },
  methods: {
    async fetchGame() {
      try {
        const response = await fetch(`http://localhost:8000/games?date=${this.birthdate}`);
        const data = await response.json();
        if (!response.ok) {
          if(response.status === 404) {
            this.game = null;
            this.found = false;
            return;
          }
          throw new Error(data.message || 'Failed to fetch game');
        }
        this.game = data;
        this.found = true;
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