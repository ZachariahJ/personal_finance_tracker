<script setup lang="ts">
import Menu from "./components/Menu.vue";
</script>

<template>
  <div class="left">
    <Menu/>
  </div>
  <div class="right">
    <router-view/>
  </div>
</template>

<style scoped lang="scss">
@import "./assets/css/vars.scss";

.left {
  position: relative;
  width: 300px;
  height: 100vh;
  border-right: 2px solid $color-primary;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.right {
  position: relative;
  width: calc(100vw - 200px);
  height: 100vh;
}
</style>
