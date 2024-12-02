<script setup lang="ts">
defineProps({
  text: String,
  link: String,
})
</script>
<template>
  <div class="absolute right-10px bottom-10px">
    <a target="_blank" :href="link"> {{ text }} </a>
  </div>
</template>

<style scoped>
.absolute {
  position: absolute;
  right: 30px;
  bottom: 30px;
}
</style>