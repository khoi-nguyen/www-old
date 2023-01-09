<template>
  <div>{{ date }}<br />{{ time }}</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";

let date = ref<String>("");
let time = ref<String>("");

function updateTime(): void {
  const now = new Date();
  const hh = now.getHours();
  const mm = now.getMinutes();
  const addZero = (n: number): String => (n < 10 ? "0" : "") + String(n);
  date.value = now.toDateString();
  time.value = addZero(hh) + ":" + addZero(mm);
}

onMounted(() => {
  updateTime();
  setInterval(updateTime, 1000);
});
</script>
