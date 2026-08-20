<script setup>
import TopNavBar from '@/components/layout/TopNavBar.vue'
import BottomNavBar from '@/components/layout/BottomNavBar.vue'
</script>

<template>
  <div class="bg-background text-on-background min-h-screen font-body-md overflow-x-hidden">
    <TopNavBar />
    <slot />
    <BottomNavBar />
  </div>
</template>
