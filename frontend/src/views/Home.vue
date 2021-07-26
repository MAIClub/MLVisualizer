<template>
  <div>
    <router-link to="/preprocessing">
      <button>Data Preprocessing</button></router-link
    >
    <router-link to="/algorithms">
      <button>Machine Learning</button></router-link
    >
    <router-link to="/log"> <button>History</button></router-link>
  </div>
</template>

<script></script>

<style lang="scss">
.main {
  margin-top: 3em;
  color: white;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

.container {
  max-width: 1000px;
  margin: 3em;
  &__top {
    display: flex;
    justify-content: center;
    height: 100%;
    &__menu {
      margin-right: 5em;
    }
  }
  &__bottom {
    display: flex;
    justify-content: center;
    margin-top: 0px;
  }
}
</style>
