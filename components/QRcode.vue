

<script setup lang="ts">
defineProps<{
  title: string,
  source: string
}>();

</script>

<template>
  <div>
    {{ title }}

    <img style="height: 300px;" :src="source" />
  </div>
</template>


