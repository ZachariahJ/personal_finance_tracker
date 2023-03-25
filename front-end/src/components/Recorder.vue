<template>
  <div class="recorder">
    <div class="input">
      <input
        @focus="isFocus = true"
        @blur="isFocus = false"
        ref="input"
        type="text"
        placeholder="e.g. eating cost 19"
      />
    </div>
    <div class="btn" @click="clickSend">Send</div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import { addTally, totalMoney, Transaction } from "../api/api";

const input = ref<HTMLInputElement | null>(null);
const isFocus = ref(false);

const props = defineProps<{
  width: string;
  tally: { data: Transaction[]; balance: number; income: number; expense: number };
}>();

// listen to user when hit the space key
const handleSpace = (e: KeyboardEvent) => {
  if (e.code === "Space") {
    if (input.value && !isFocus.value) {
      e.preventDefault();
      input.value.focus();
    }
  } else if (e.code === "Enter") {
    e.preventDefault();
    if (isFocus.value) {
      clickSend();
    }
  }
};

const clickSend = async () => {
  input.value?.blur();
  props.tally.data = await addTally((input.value as HTMLInputElement).value);
  console.log(props.tally.data);
  const lastItem = props.tally.data[props.tally.data.length - 1];
  if (lastItem.amount >= 0) {
    props.tally.income += lastItem.amount;
  } else {
    props.tally.expense -= lastItem.amount;
  }
  props.tally.balance = await totalMoney();
  (input.value as HTMLInputElement).value = "";
  // const scrollableElement = document.getElementById("table")!;
  // const scrollHeight = scrollableElement.scrollHeight;
  // const scrollTop = scrollableElement.scrollTop;
  // const clientHeight = scrollableElement.clientHeight;
  // const isAtBottom = scrollHeight - scrollTop === clientHeight;

  // if (!isAtBottom) {
  //   scrollableElement.scrollTop = scrollHeight - clientHeight;
  // }

  // setTimeout(() => {
  //   if (!isAtBottom) {
  //     scrollableElement.scrollTop = scrollHeight - clientHeight;
  //   }
  // }, 1000);
};

onMounted(() => {
  window.addEventListener("keydown", handleSpace);
});
</script>

<style lang="scss" scoped>
@import "@/assets/css/vars.scss";
.recorder {
  width: v-bind(width);
  margin: 20px auto;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .input {
    width: 100%;

    input {
      width: 100%;
      height: 40px;
      border: 1px solid $color-primary;
      border-radius: 20px;
      padding: 0 20px;
      transition: all 0.1s ease-in-out;

      &:focus {
        outline: none;
        border: 2px solid $color-tertiary;
      }
    }
  }

  .btn {
    margin-left: 20px;
    width: 100px;
    height: 40px;
    background-color: $color-primary;
    border-radius: 20px;
    color: $white;
    display: flex;
    justify-content: center;
    transition: all 0.1s ease-in-out;
    align-items: center;
    cursor: pointer;

    &:hover {
      background-color: $color-primary-light;
    }
  }
}
</style>
