document.addEventListener('DOMContentLoaded', function () {
  const dropZone = document.getElementById('dropZone');
  const fileInput = document.getElementById('fileInput');
  const fileInfo = document.getElementById('fileInfo');
  const fileName = document.getElementById('fileName');
  const removeFile = document.getElementById('removeFile');
  const uploadForm = document.getElementById('uploadForm');
  const submitBtn = document.getElementById('submitBtn');
  const loading = document.getElementById('loading');
  const results = document.getElementById('results');
  const resultContent = document.getElementById('resultContent');
  const resultInfo = document.getElementById('resultInfo');
  const copyBtn = document.getElementById('copyBtn');

  let selectedFile = null;

  // Drag and drop functionality
  dropZone.addEventListener('dragover', function (e) {
    e.preventDefault();
    dropZone.classList.add('dragover');
  });

  dropZone.addEventListener('dragleave', function (e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');
  });

  dropZone.addEventListener('drop', function (e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileSelect(files[0]);
    }
  });

  // Click to browse
  dropZone.addEventListener('click', function () {
    fileInput.click();
  });

  fileInput.addEventListener('change', function (e) {
    if (e.target.files.length > 0) {
      handleFileSelect(e.target.files[0]);
    }
  });

  // Remove file
  removeFile.addEventListener('click', function () {
    selectedFile = null;
    fileInput.value = '';
    fileInfo.classList.add('hidden');
    submitBtn.disabled = true;
    results.classList.add('hidden');
  });

  function handleFileSelect(file) {
    selectedFile = file;
    fileName.textContent = file.name;
    fileInfo.classList.remove('hidden');
    submitBtn.disabled = false;
    results.classList.add('hidden');
  }

  // Form submission
  uploadForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    if (!selectedFile) {
      alert('Please select a file first.');
      return;
    }

    // Show loading
    loading.classList.add('show');
    submitBtn.disabled = true;
    results.classList.add('hidden');

    // Prepare form data
    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('use_llm', document.getElementById('useLLM').checked);
    formData.append('force_ocr', document.getElementById('forceOCR').checked);
    formData.append('debug', document.getElementById('debug').checked);

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData
      });

      const result = await response.json();

      if (response.ok) {
        // Show results
        resultContent.textContent = result.markdown;
        resultInfo.textContent = `Parsed: ${result.filename} (${result.content_type})`;
        results.classList.remove('hidden');

        // Scroll to results
        results.scrollIntoView({ behavior: 'smooth' });
      } else {
        alert(`Error: ${result.detail || 'Failed to parse file'}`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while processing the file.');
    } finally {
      // Hide loading
      loading.classList.remove('show');
      submitBtn.disabled = false;
    }
  });

  // Copy button
  copyBtn.addEventListener('click', function () {
    navigator.clipboard.writeText(resultContent.textContent).then(function () {
      const originalText = copyBtn.innerHTML;
      copyBtn.innerHTML = '<i class="fas fa-check mr-2"></i>Copied!';
      setTimeout(function () {
        copyBtn.innerHTML = originalText;
      }, 2000);
    }).catch(function (err) {
      console.error('Could not copy text: ', err);
      alert('Failed to copy text to clipboard');
    });
  });
});
