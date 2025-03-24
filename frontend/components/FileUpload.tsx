import { useState } from 'react'
import { useSupabaseClient } from '@supabase/auth-helpers-react'
import { Upload, Loader } from 'lucide-react'
import { Button } from './ui/button'
import { toast } from './ui/toast'

export function FileUpload() {
  const [files, setFiles] = useState<File[]>([])
  const [uploading, setUploading] = useState(false)
  const supabase = useSupabaseClient()

  const handleUpload = async (files: FileList | null) => {
    if (!files) return

    setUploading(true)
    const formData = new FormData()
    Array.from(files).forEach(file => {
      formData.append('files', file)
    })

    try {
      const response = await fetch('http://localhost:8000/files/upload', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) throw new Error('Upload failed')

      const data = await response.json()
      toast({
        title: 'Success',
        description: `Uploaded ${files.length} files successfully`,
      })
    } catch (error) {
      console.error('Upload failed:', error)
      toast({
        title: 'Error',
        description: 'Failed to upload files',
        variant: 'destructive',
      })
    } finally {
      setUploading(false)
    }
  }

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="border-2 border-dashed rounded-lg p-8 text-center">
        {uploading ? (
          <Loader className="animate-spin h-12 w-12 mx-auto text-primary" />
        ) : (
          <>
            <Upload className="mx-auto h-12 w-12 text-gray-400" />
            <input
              type="file"
              multiple
              accept=".pdf"
              onChange={(e) => handleUpload(e.target.files)}
              className="hidden"
              id="file-upload"
            />
            <label htmlFor="file-upload" className="cursor-pointer">
              <span className="mt-2 block text-sm font-medium">
                Drop PDF files here or click to upload
              </span>
            </label>
          </>
        )}
      </div>
    </div>
  )
} 