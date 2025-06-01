<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نمایش فایل‌های پوشه</title>
    <style>
        body {
            font-family: 'Tahoma', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .path-info {
            background: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 20px;
            font-family: monospace;
            word-break: break-all;
        }
        .file-list {
            list-style: none;
            padding: 0;
        }
        .file-item {
            padding: 10px;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
        }
        .file-item:hover {
            background-color: #f8f9fa;
        }
        .icon {
            margin-left: 10px;
            font-size: 18px;
        }
        .folder {
            color: #2980b9;
            font-weight: bold;
        }
        .file {
            color: #34495e;
        }
        .file-size {
            color: #7f8c8d;
            font-size: 0.8em;
            margin-right: 15px;
        }
        .file-date {
            color: #7f8c8d;
            font-size: 0.8em;
            margin-right: auto;
        }
        .actions {
            display: flex;
            gap: 10px;
        }
        .actions a {
            color: #3498db;
            text-decoration: none;
            font-size: 0.9em;
        }
        .actions a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>لیست فایل‌های پوشه</h1>
        
        <?php
        // دریافت مسیر فعلی
        $currentDir = getcwd();
        echo '<div class="path-info">مسیر جاری: <strong>' . htmlspecialchars($currentDir) . '</strong></div>';
        
        // خواندن محتویات پوشه
        $files = scandir($currentDir);
        
        if ($files === false) {
            echo '<p>خطا در خواندن محتویات پوشه</p>';
        } else {
            echo '<ul class="file-list">';
            
            // حذف . و .. از لیست
            $files = array_diff($files, array('.', '..'));
            
            foreach ($files as $file) {
                $filePath = $currentDir . DIRECTORY_SEPARATOR . $file;
                $isDir = is_dir($filePath);
                
                echo '<li class="file-item ' . ($isDir ? 'folder' : 'file') . '">';
                echo '<span class="icon">' . ($isDir ? '📁' : '📄') . '</span>';
                echo '<span class="file-name">' . htmlspecialchars($file) . '</span>';
                
                if (!$isDir) {
                    $fileSize = filesize($filePath);
                    echo '<span class="file-size">' . formatSizeUnits($fileSize) . '</span>';
                }
                
                $fileDate = date("Y-m-d H:i:s", filemtime($filePath));
                echo '<span class="file-date">' . $fileDate . '</span>';
                
                echo '<div class="actions">';
                if ($isDir) {
                    echo '<a href="?dir=' . urlencode($file) . '">ورود</a>';
                } else {
                    echo '<a href="' . htmlspecialchars($file) . '" download>دانلود</a>';
                }
                echo '</div>';
                
                echo '</li>';
            }
            
            echo '</ul>';
        }
        
        // تابع برای فرمت‌دهی سایز فایل
        function formatSizeUnits($bytes) {
            if ($bytes >= 1073741824) {
                $bytes = number_format($bytes / 1073741824, 2) . ' GB';
            } elseif ($bytes >= 1048576) {
                $bytes = number_format($bytes / 1048576, 2) . ' MB';
            } elseif ($bytes >= 1024) {
                $bytes = number_format($bytes / 1024, 2) . ' KB';
            } elseif ($bytes > 1) {
                $bytes = $bytes . ' bytes';
            } elseif ($bytes == 1) {
                $bytes = $bytes . ' byte';
            } else {
                $bytes = '0 bytes';
            }
            return $bytes;
        }
        ?>
    </div>
</body>
</html>
