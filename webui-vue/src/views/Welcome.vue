<template>
  <div class="welcome-container">
    <!-- Hero Section (紧凑版) -->
    <div class="hero-section">
      <div class="hero-content">
        <a href="https://github.com/None9527/None_Z-image-Turbo_trainer" target="_blank" class="title-link">
          <div class="logo-icon">
            <span class="logo-text">N</span>
          </div>
          <h1 class="main-title">
            <span class="title-gradient">None</span> Trainer
          </h1>
        </a>
        <p class="tagline">Z-Image Turbo LoRA 训练工作室 · 基于 <strong>AC-RF</strong> 算法</p>
        <div class="feature-tags">
          <span class="tag"><el-icon><Lightning /></el-icon> 10步推理</span>
          <span class="tag"><el-icon><Cpu /></el-icon> 硬件优化</span>
          <span class="tag"><el-icon><TrendCharts /></el-icon> 实时监控</span>
        </div>
      </div>
    </div>

    <!-- Dashboard Grid -->
    <div class="dashboard-grid">
      <!-- Quick Actions (4列) -->
      <div class="card glass-card quick-actions">
        <div class="action-buttons">
          <div class="action-item" @click="$router.push('/dataset')">
            <div class="action-icon dataset"><el-icon><Picture /></el-icon></div>
            <div class="action-info">
              <span class="action-name">数据集</span>
              <span class="action-desc">导入、缓存、标注</span>
            </div>
            <el-icon class="arrow"><ArrowRight /></el-icon>
          </div>
          <div class="action-item" @click="$router.push('/config')">
            <div class="action-icon config"><el-icon><Setting /></el-icon></div>
            <div class="action-info">
              <span class="action-name">配置</span>
              <span class="action-desc">参数、LoRA、优化</span>
            </div>
            <el-icon class="arrow"><ArrowRight /></el-icon>
          </div>
          <div class="action-item" @click="$router.push('/training')">
            <div class="action-icon train"><el-icon><VideoPlay /></el-icon></div>
            <div class="action-info">
              <span class="action-name">训练</span>
              <span class="action-desc">Loss、进度监控</span>
            </div>
            <el-icon class="arrow"><ArrowRight /></el-icon>
          </div>
          <div class="action-item" @click="$router.push('/generation')">
            <div class="action-icon generate"><el-icon><MagicStick /></el-icon></div>
            <div class="action-info">
              <span class="action-name">生成</span>
              <span class="action-desc">测试 LoRA</span>
            </div>
            <el-icon class="arrow"><ArrowRight /></el-icon>
          </div>
        </div>
      </div>

      <!-- System Status (紧凑) -->
      <div class="card glass-card system-status">
        <h3 class="card-title">
          <el-icon><Monitor /></el-icon> 系统
          <el-tag v-if="wsConnected" type="success" size="small" effect="plain">在线</el-tag>
          <el-tag v-else type="danger" size="small" effect="plain">离线</el-tag>
        </h3>
        <div class="status-grid" v-if="hasSystemInfo">
          <div class="status-item">
            <span class="label">Python</span>
            <span class="value">{{ systemInfo.python }}</span>
          </div>
          <div class="status-item">
            <span class="label">PyTorch</span>
            <span class="value">{{ systemInfo.pytorch }}</span>
          </div>
          <div class="status-item">
            <span class="label">CUDA</span>
            <span class="value">{{ systemInfo.cuda }}</span>
          </div>
          <div class="status-item">
            <span class="label">Diffusers</span>
            <span class="value">{{ systemInfo.diffusers }}</span>
          </div>
        </div>
        <div v-else class="loading-placeholder">
          <el-icon class="is-loading"><Loading /></el-icon>
          <span>连接中...</span>
        </div>
      </div>

      <!-- Model Status (紧凑) -->
      <div class="card glass-card model-card">
        <h3 class="card-title">
          <el-icon><Box /></el-icon> 模型
          <el-tag :type="modelStatus.exists ? 'success' : 'warning'" size="small" effect="dark">
            {{ modelStatus.exists ? '就绪' : '需下载' }}
          </el-tag>
        </h3>
        
        <div class="model-compact" v-if="modelStatus.summary">
          <div class="model-progress-mini">
            <svg viewBox="0 0 36 36">
              <circle class="bg" cx="18" cy="18" r="15.5" />
              <circle class="progress" cx="18" cy="18" r="15.5" :style="{ strokeDashoffset: progressOffsetMini }" />
            </svg>
            <span class="progress-num">{{ validPercent }}%</span>
          </div>
          <div class="component-mini">
            <span v-for="(comp, name) in modelStatus.details" :key="name" class="comp-dot" :class="{ valid: comp.valid }">
              <el-icon v-if="comp.valid"><CircleCheck /></el-icon>
              <el-icon v-else><Close /></el-icon>
            </span>
          </div>
        </div>

        <div class="model-actions" v-if="!modelStatus.exists">
          <el-button v-if="!isDownloading" type="primary" size="small" @click="startDownload" :loading="startingDownload">
            <el-icon><Download /></el-icon> 下载模型
          </el-button>
          <div v-else class="download-status">
            <el-progress :percentage="downloadProgress" :stroke-width="6" />
            <span class="download-text">{{ downloadSizeText }}</span>
          </div>
        </div>
      </div>

      <!-- Tech & Contact (合并) -->
      <div class="card glass-card info-card">
        <div class="info-split">
          <div class="tech-section">
            <div class="highlight"><span>🎯</span> 锚点耦合</div>
            <div class="highlight"><span>📉</span> Min-SNR</div>
            <div class="highlight"><span>⚡</span> Flash Attn</div>
            <div class="highlight"><span>🔧</span> 硬件适配</div>
          </div>
          <div class="contact-section">
            <div class="contact-row" @click="copyEmail('lihaonan1082@gmail.com')">
              <span>📧</span> lihaonan1082@gmail.com
            </div>
            <div class="contact-row" @click="copyEmail('592532681@qq.com')">
              <span>📮</span> 592532681@qq.com
            </div>
          </div>
        </div>
        <div class="author">Made with ❤️ by <strong>None</strong></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useSystemStore } from '@/stores/system'
import { useWebSocketStore } from '@/stores/websocket'
import { 
  Picture, Setting, VideoPlay, Cpu,
  CircleCheck, Close, Loading, Box, Monitor,
  ArrowRight, MagicStick, Download, Lightning, TrendCharts
} from '@element-plus/icons-vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'

const systemStore = useSystemStore()
const wsStore = useWebSocketStore()

const modelStatus = ref({ exists: false, details: null as any, summary: null as any })
const startingDownload = ref(false)

const systemInfo = computed(() => systemStore.systemInfo)
const wsConnected = computed(() => wsStore.isConnected)
const hasSystemInfo = computed(() => systemStore.systemInfo.python !== '')

const downloadStatus = computed(() => systemStore.downloadStatus)
const isDownloading = computed(() => downloadStatus.value.status === 'running')
const downloadProgress = computed(() => downloadStatus.value.progress)
const downloadSizeText = computed(() => {
  const gb = downloadStatus.value.downloaded_size_gb || 0
  return gb > 0 ? `${gb.toFixed(1)} GB` : '准备中...'
})

const validPercent = computed(() => {
  if (!modelStatus.value.summary) return 0
  const { valid_components, total_components } = modelStatus.value.summary
  return Math.round((valid_components / total_components) * 100)
})

const progressOffsetMini = computed(() => {
  const circumference = 2 * Math.PI * 15.5
  return circumference - (validPercent.value / 100) * circumference
})

async function refreshModelStatus() {
  try {
    const res = await axios.get('/api/system/model-status')
    modelStatus.value = res.data
  } catch (e) {
    console.error('Failed to check model status:', e)
  }
}

async function startDownload() {
  startingDownload.value = true
  try {
    await axios.post('/api/system/download-model')
    ElMessage.success('下载任务已启动')
  } catch (e: any) {
    ElMessage.error('启动下载失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    startingDownload.value = false
  }
}

refreshModelStatus()

function copyEmail(email: string) {
  navigator.clipboard.writeText(email)
  ElMessage.success(`已复制: ${email}`)
}
</script>

<style scoped>
.welcome-container {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
  overflow: hidden;
}

/* Hero Section - 紧凑 */
.hero-section {
  padding: 24px 40px 16px;
  text-align: center;
  background: linear-gradient(180deg, rgba(240, 180, 41, 0.03) 0%, transparent 100%);
  flex-shrink: 0;
}

.title-link {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.title-link:hover {
  transform: scale(1.02);
}

.title-link:hover .logo-icon {
  box-shadow: 0 8px 30px rgba(240, 180, 41, 0.4);
}

.title-link:hover .main-title {
  text-shadow: 0 0 20px rgba(240, 180, 41, 0.3);
}

.logo-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #f0b429 0%, #e67e22 100%);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 24px rgba(240, 180, 41, 0.3);
  margin-bottom: 8px;
  transition: box-shadow 0.3s;
}

.logo-text {
  font-size: 32px;
  font-weight: 800;
  color: #1a1a1d;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 800;
  margin: 0 0 4px 0;
  letter-spacing: -1px;
  transition: text-shadow 0.3s;
}

.title-gradient {
  background: linear-gradient(135deg, #f0b429 0%, #f39c12 50%, #e67e22 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.tagline {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin: 0 0 12px 0;
}

.tagline strong {
  color: var(--primary);
}

.feature-tags {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.feature-tags .tag {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 5px 12px;
  background: rgba(240, 180, 41, 0.1);
  border: 1px solid rgba(240, 180, 41, 0.2);
  border-radius: 16px;
  font-size: 12px;
  color: var(--text-secondary);
}

.feature-tags .tag .el-icon {
  color: var(--primary);
  font-size: 12px;
}

/* Dashboard Grid - 紧凑2x2 */
.dashboard-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: auto 1fr;
  gap: 16px;
  padding: 0 40px 24px;
  max-width: 1100px;
  margin: 0 auto;
  width: 100%;
  min-height: 0;
}

/* Cards */
.card {
  padding: 16px;
  border-radius: 12px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  min-height: 0;
  overflow: hidden;
}

.card-title {
  display: flex;
  align-items: center;
  gap: 6px;
  margin: 0 0 12px 0;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
}

.card-title .el-icon {
  color: var(--primary);
}

.card-title .el-tag {
  margin-left: auto;
}

/* Quick Actions - 横向4列 */
.quick-actions {
  grid-column: 1 / -1;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.action-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px;
  background: var(--bg-darker);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-item:hover {
  border-color: var(--primary);
  background: rgba(240, 180, 41, 0.05);
  transform: translateY(-2px);
}

.action-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
}

.action-icon.dataset { background: rgba(64, 158, 255, 0.15); color: #409eff; }
.action-icon.config { background: rgba(103, 194, 58, 0.15); color: #67c23a; }
.action-icon.train { background: rgba(240, 180, 41, 0.15); color: #f0b429; }
.action-icon.generate { background: rgba(230, 126, 34, 0.15); color: #e67e22; }

.action-info {
  flex: 1;
  min-width: 0;
}

.action-name {
  font-weight: 600;
  font-size: 13px;
  color: var(--text-primary);
  display: block;
}

.action-desc {
  font-size: 11px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.action-item .arrow {
  color: var(--text-muted);
  transition: transform 0.2s;
  flex-shrink: 0;
}

.action-item:hover .arrow {
  color: var(--primary);
  transform: translateX(3px);
}

/* System Status - 紧凑 */
.status-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 10px;
  background: var(--bg-darker);
  border-radius: 6px;
}

.status-item .label {
  color: var(--text-muted);
  font-size: 11px;
}

.status-item .value {
  color: var(--text-primary);
  font-weight: 500;
  font-size: 11px;
  font-family: var(--font-mono);
}

.loading-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 20px;
  color: var(--text-muted);
  font-size: 12px;
}

/* Model Card - 紧凑 */
.model-compact {
  display: flex;
  align-items: center;
  gap: 16px;
}

.model-progress-mini {
  position: relative;
  width: 48px;
  height: 48px;
  flex-shrink: 0;
}

.model-progress-mini svg {
  transform: rotate(-90deg);
  width: 100%;
  height: 100%;
}

.model-progress-mini circle {
  fill: none;
  stroke-width: 3;
  stroke-linecap: round;
}

.model-progress-mini .bg { stroke: var(--bg-darker); }
.model-progress-mini .progress {
  stroke: var(--success);
  stroke-dasharray: 97.4;
  transition: stroke-dashoffset 0.5s ease;
}

.progress-num {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 11px;
  font-weight: 700;
  color: var(--text-primary);
}

.component-mini {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.comp-dot {
  width: 20px;
  height: 20px;
  border-radius: 4px;
  background: var(--bg-darker);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  color: var(--text-muted);
}

.comp-dot.valid {
  background: rgba(103, 194, 58, 0.15);
  color: var(--success);
}

.model-actions {
  margin-top: 12px;
}

.download-status {
  max-width: 200px;
}

.download-text {
  display: block;
  margin-top: 4px;
  font-size: 11px;
  color: var(--text-muted);
  text-align: center;
}

/* Info Card - 合并技术和联系 */
.info-card {
  display: flex;
  flex-direction: column;
}

.info-split {
  flex: 1;
  display: flex;
  gap: 16px;
}

.tech-section {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}

.highlight {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 10px;
  background: var(--bg-darker);
  border-radius: 6px;
  font-size: 11px;
  color: var(--text-secondary);
}

.highlight span:first-child {
  font-size: 14px;
}

.contact-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.contact-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  background: var(--bg-darker);
  border-radius: 6px;
  font-size: 11px;
  color: var(--text-secondary);
  font-family: var(--font-mono);
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid transparent;
}

.contact-row:hover {
  border-color: var(--primary);
  color: var(--text-primary);
}

.contact-row span:first-child {
  font-size: 14px;
}

.author {
  text-align: center;
  padding-top: 10px;
  margin-top: auto;
  color: var(--text-muted);
  font-size: 11px;
  border-top: 1px solid var(--border-color);
}

.author strong {
  color: var(--primary);
}

/* Responsive */
@media (max-width: 900px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
    padding: 0 16px 16px;
  }
  
  .hero-section {
    padding: 16px;
  }
  
  .main-title {
    font-size: 2rem;
  }
  
  .action-buttons {
    grid-template-columns: 1fr 1fr;
  }
  
  .info-split {
    flex-direction: column;
  }
}
</style>
