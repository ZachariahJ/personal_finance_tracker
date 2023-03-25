<script setup lang="ts">
import { ref } from "vue";

// defineProps<{ msg: string }>()
</script>

<template>
  <div class="logo">
    <img src="/vite.svg" alt="logo" />
    <h1><router-link to="/my-wallet">Tally</router-link></h1>
  </div>
  <div class="menus">
    <router-link class="menu bb" active-class="selected" to="/my-wallet"
      >My Wallet</router-link
    >
    <router-link class="menu bb" active-class="selected" to="/calender"
      >Calender</router-link
    >
    <router-link class="menu bb" active-class="selected" to="/auto-billing"
      >Auto-Billing</router-link
    >
    <router-link class="menu" active-class="selected" to="/charts"
      >Charts</router-link
    >
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/css/vars.scss";

.logo {
  display: flex;
  width: 100%;
  height: 60px;
  justify-content: center;
  align-items: center;
  border-bottom: 2px solid $color-primary;

  img {
    height: 35px;
  }

  h1 {
    color: $color-primary;
    margin-left: 20px;
  }
}

.menus {
  display: block;
  flex-direction: column;
  width: 100%;

  .menu {
    display: flex;
    width: 100%;
    height: 40px;
    justify-content: center;
    align-items: center;
    transition: all .2s ease-in-out;
  }
}

.bb {
  border-bottom: 1px solid $color-primary;
}

.selected {
  background-color: $color-primary;
  color: $white;
}
</style>
