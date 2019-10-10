# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import zipfile
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings

class Mp3DownloadPipeline(FilesPipeline):
    def item_completed(self, results, item, info):
        settings = get_project_settings()
        base_path = settings.get('FILES_STORE')
        rel_path = [x['path'] for ok, x in results if ok]
        
        # Extract zip file only if album is available
        if rel_path:
            abs_path = base_path+'/'+rel_path[0]
            with zipfile.ZipFile(abs_path, 'r') as zip_ref:
                zip_ref.extractall(base_path)

        return super().item_completed(results, item, info)
