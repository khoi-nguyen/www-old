<template>
  <object
    ref="object"
    type="application/pdf"
    :data="url"
    :width="width"
    :height="_height"
  >
    <embed :src="url" />
  </object>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from "vue";

type dim = `${number}%` | number;

interface Props {
  height: dim;
  mode?: "A4";
  page?: number;
  src: string;
  width: dim;
}

const props = withDefaults(defineProps<Props>(), {
  height: 900,
  page: 1,
  width: "100%",
});
const _height = ref<dim>(0);
const object = ref<null | HTMLElement>(null);

const url = computed(() => {
  let url: string = props.src;
  if (props.mode === "A4") {
    url += `#view=FitH&toolbar=0&page=${props.page}`;
  }
  return url;
});

onMounted(() => {
  _height.value = props.height;
  if (props.mode === "A4") {
    const resizeObserver = new ResizeObserver(() => {
      _height.value = 1.414 * object.value.offsetWidth;
    });
    resizeObserver.observe(object.value);
  }
});
</script>
