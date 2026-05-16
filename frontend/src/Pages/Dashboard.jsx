// src/pages/Dashboard.jsx

import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import axios from 'axios'

import {
  Sparkles,
  FileText,
  Newspaper,
  PenSquare,
  BarChart3,
  Download,
  ImageIcon,
  Search,
  Wand2,
  CheckCircle2,
  Loader2,
} from 'lucide-react'


// ============================================================
// API
// ============================================================

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000',
})


// ============================================================
// CONTENT TYPES
// ============================================================

const contentTypes = [
  {
    id: 'seo_blog',
    title: 'SEO Blog',
    icon: FileText,
  },

  {
    id: 'newsletter',
    title: 'Newsletter',
    icon: Newspaper,
  },

  {
    id: 'linkedin_post',
    title: 'LinkedIn',
    icon: PenSquare,
  },

  {
    id: 'marketing_copy',
    title: 'Marketing',
    icon: Sparkles,
  },

  {
    id: 'research_report',
    title: 'Research',
    icon: BarChart3,
  },
]


// ============================================================
// COMPONENT
// ============================================================

export default function Dashboard() {

  // ==========================================================
  // STATE
  // ==========================================================

  const [topic, setTopic] = useState('')

  const [contentType, setContentType] =
    useState('seo_blog')

  const [tone, setTone] =
    useState('professional')

  const [generateImages, setGenerateImages] =
    useState(true)

  const [loading, setLoading] =
    useState(false)

  const [queries, setQueries] =
    useState([])

  const [article, setArticle] =
    useState('')

  const [images, setImages] =
    useState([])

  const [pdfPath, setPdfPath] =
    useState('')

  const [error, setError] =
    useState('')

  const [currentStep, setCurrentStep] =
    useState('Idle')


  // ==========================================================
  // GENERATE CONTENT
  // ==========================================================

  const generateContent = async () => {

    try {

      setLoading(true)

      setError('')

      setQueries([])

      setArticle('')

      setImages([])

      setPdfPath('')

      // ======================================================
      // SIMULATED LIVE PIPELINE
      // ======================================================

      setCurrentStep('Generating search queries...')

      const response = await API.post(
        '/generate',
        {
          topic,
          content_type: contentType,
          tone,
          generate_images: generateImages,
        }
      )

      const data = response.data

      // ======================================================
      // QUERIES
      // ======================================================

      setCurrentStep('Researching web sources...')

      if (data.queries) {

        for (let q of data.queries) {

          await new Promise((r) =>
            setTimeout(r, 120)
          )

          setQueries((prev) => [...prev, q])
        }
      }

      // ======================================================
      // ARTICLE
      // ======================================================

      setCurrentStep('Writing content...')

      await new Promise((r) =>
        setTimeout(r, 700)
      )

      setArticle(data.article || '')

      // ======================================================
      // SEO
      // ======================================================

      setCurrentStep('Optimizing SEO...')

      await new Promise((r) =>
        setTimeout(r, 600)
      )

      // ======================================================
      // IMAGES
      // ======================================================

      if (generateImages) {

        setCurrentStep(
          'Generating AI visuals...'
        )

        await new Promise((r) =>
          setTimeout(r, 700)
        )

        setImages(data.images || [])
      }

      // ======================================================
      // PDF
      // ======================================================

      setCurrentStep('Exporting PDF...')

      await new Promise((r) =>
        setTimeout(r, 500)
      )

      setPdfPath(data.pdf_path || '')

      setCurrentStep('Completed')

    } catch (err) {

      console.error(err)

      setError('Generation failed.')

    } finally {

      setLoading(false)
    }
  }


  // ==========================================================
  // UI
  // ==========================================================

  return (

    <div className="
      min-h-screen
      bg-[#060606]
      text-white
      flex
    ">

      {/* ==================================================== */}
      {/* SIDEBAR */}
      {/* ==================================================== */}

      <div className="
        w-[380px]
        border-r
        border-zinc-800
        bg-[#0b0b0b]
        p-7
        overflow-y-auto
      ">

        {/* LOGO */}

        <div className="mb-10">

          <div className="
            flex
            items-center
            gap-3
          ">

            <div className="
              w-12
              h-12
              rounded-2xl
              bg-blue-600
              flex
              items-center
              justify-center
            ">

              <Sparkles size={22} />

            </div>

            <div>

              <h1 className="
                text-3xl
                font-bold
                tracking-tight
              ">
                StudioAI
              </h1>

              <p className="
                text-zinc-500
                text-sm
              ">
                Agentic AI Content Engine
              </p>
            </div>
          </div>
        </div>


        {/* TOPIC INPUT */}

        <div className="mb-8">

          <label className="
            text-sm
            text-zinc-400
            mb-3
            block
          ">
            Content Topic
          </label>

          <textarea
            value={topic}
            onChange={(e) =>
              setTopic(e.target.value)
            }
            placeholder="
Write your topic here...

Example:
The Rise of Autonomous AI Agents
"
            className="
              w-full
              h-40
              bg-zinc-900
              border
              border-zinc-800
              rounded-3xl
              p-5
              resize-none
              outline-none
              focus:border-blue-500
              transition-all
            "
          />
        </div>


        {/* CONTENT TYPES */}

        <div className="mb-8">

          <h2 className="
            text-sm
            text-zinc-400
            mb-4
          ">
            Content Type
          </h2>

          <div className="
            grid
            grid-cols-2
            gap-3
          ">

            {contentTypes.map((item) => {

              const Icon = item.icon

              return (

                <button
                  key={item.id}
                  onClick={() =>
                    setContentType(item.id)
                  }
                  className={`
                    p-4
                    rounded-2xl
                    border
                    transition-all
                    text-left

                    ${contentType === item.id
                      ? 'bg-blue-600 border-blue-500'
                      : 'bg-zinc-900 border-zinc-800 hover:border-zinc-700'
                    }
                  `}
                >

                  <Icon size={20} />

                  <p className="
                    mt-3
                    font-medium
                    text-sm
                  ">
                    {item.title}
                  </p>
                </button>
              )
            })}
          </div>
        </div>


        {/* TONE */}

        <div className="mb-8">

          <label className="
            text-sm
            text-zinc-400
            mb-3
            block
          ">
            Tone
          </label>

          <select
            value={tone}
            onChange={(e) =>
              setTone(e.target.value)
            }
            className="
              w-full
              bg-zinc-900
              border
              border-zinc-800
              rounded-2xl
              p-4
              outline-none
            "
          >

            <option value="professional">
              Professional
            </option>

            <option value="technical">
              Technical
            </option>

            <option value="casual">
              Casual
            </option>

            <option value="persuasive">
              Persuasive
            </option>

          </select>
        </div>


        {/* IMAGE TOGGLE */}

        <div className="
          mb-8
          bg-zinc-900
          border
          border-zinc-800
          rounded-3xl
          p-5
        ">

          <div className="
            flex
            items-center
            justify-between
          ">

            <div>

              <div className="
                flex
                items-center
                gap-2
              ">

                <ImageIcon size={18} />

                <h3 className="
                  font-semibold
                ">
                  AI Visuals
                </h3>
              </div>

              <p className="
                text-sm
                text-zinc-500
                mt-2
              ">
                Generate images automatically
              </p>
            </div>


            <button
              onClick={() =>
                setGenerateImages(
                  !generateImages
                )
              }
              className={`
                relative
                w-16
                h-9
                rounded-full
                transition-all

                ${generateImages
                  ? 'bg-blue-600'
                  : 'bg-zinc-700'
                }
              `}
            >

              <div
                className={`
                  absolute
                  top-1.5
                  w-6
                  h-6
                  rounded-full
                  bg-white
                  transition-all

                  ${generateImages
                    ? 'translate-x-8'
                    : 'translate-x-1'
                  }
                `}
              />

            </button>
          </div>
        </div>


        {/* GENERATE BUTTON */}

        <button
          onClick={generateContent}
          disabled={loading}
          className="
            w-full
            py-5
            rounded-3xl
            bg-blue-600
            hover:bg-blue-500
            transition-all
            font-semibold
            text-lg
            flex
            items-center
            justify-center
            gap-3
            disabled:opacity-50
          "
        >

          {loading
            ? (
              <>
                <Loader2
                  size={20}
                  className="animate-spin"
                />

                Generating...
              </>
            )
            : (
              <>
                <Wand2 size={20} />
                Generate Content
              </>
            )
          }

        </button>


        {/* LIVE STATUS */}

        <div className="
          mt-10
          bg-zinc-900
          border
          border-zinc-800
          rounded-3xl
          p-5
        ">

          <div className="
            flex
            items-center
            gap-2
            mb-5
          ">

            <Loader2
              size={18}
              className={loading
                ? 'animate-spin'
                : ''
              }
            />

            <h3 className="font-semibold">
              Pipeline Status
            </h3>
          </div>

          <p className="
            text-zinc-400
            text-sm
          ">
            {currentStep}
          </p>
        </div>


        {/* GENERATED QUERIES */}

        {queries.length > 0 && (

          <div className="
            mt-10
            bg-zinc-900
            border
            border-zinc-800
            rounded-3xl
            p-5
          ">

            <div className="
              flex
              items-center
              gap-2
              mb-5
            ">

              <Search size={18} />

              <h3 className="
                font-semibold
              ">
                Generated Queries
              </h3>
            </div>


            <div className="
              space-y-3
              max-h-[320px]
              overflow-y-auto
            ">

              {queries.map((query, index) => (

                <div
                  key={index}
                  className="
                    p-3
                    rounded-2xl
                    bg-black/40
                    border
                    border-zinc-800
                    text-sm
                    text-zinc-300
                  "
                >

                  {query}

                </div>
              ))}

            </div>
          </div>
        )}

      </div>


      {/* ==================================================== */}
      {/* MAIN CONTENT */}
      {/* ==================================================== */}

      <div className="
        flex-1
        overflow-y-auto
        bg-[#f4f4f5]
        text-black
      ">

        {/* HEADER */}

        <div className="
          sticky
          top-0
          z-50
          bg-white/80
          backdrop-blur-xl
          border-b
          border-zinc-200
          px-10
          py-5
          flex
          items-center
          justify-between
        ">

          <div>

            <h1 className="
              text-2xl
              font-bold
            ">
              AI Content Workspace
            </h1>

            <p className="
              text-zinc-500
              mt-1
            ">
              Real-time AI content generation
            </p>
          </div>


          {pdfPath && (

            <a
              href={`
http://127.0.0.1:8000/${pdfPath}
`}
              target="_blank"
              rel="noreferrer"
              className="
                px-6
                py-3
                rounded-2xl
                bg-black
                text-white
                flex
                items-center
                gap-3
                hover:bg-zinc-800
                transition-all
              "
            >

              <Download size={18} />

              Export PDF

            </a>
          )}
        </div>


        {/* EMPTY STATE */}

        {!article && !loading && (

          <div className="
            h-[80vh]
            flex
            items-center
            justify-center
            flex-col
            text-center
          ">

            <div className="
              w-24
              h-24
              rounded-[30px]
              bg-blue-600
              flex
              items-center
              justify-center
              mb-8
            ">

              <Sparkles size={40} />

            </div>

            <h2 className="
              text-4xl
              font-bold
            ">
              Create AI Content
            </h2>

            <p className="
              text-zinc-500
              mt-4
              max-w-xl
            ">
              Generate blogs, newsletters,
              LinkedIn posts, research reports,
              and multimodal AI content.
            </p>
          </div>
        )}


        {/* ARTICLE */}

        {article && (

          <div className="
            max-w-6xl
            mx-auto
            px-10
            py-12
          ">

            {/* SUCCESS */}

            <div className="
              mb-8
              flex
              items-center
              gap-3
              text-green-600
            ">

              <CheckCircle2 size={20} />

              <span className="
                font-medium
              ">
                Content generated successfully
              </span>
            </div>


            {/* ARTICLE CARD */}

            <div className="
              bg-white
              rounded-[32px]
              shadow-xl
              p-14
            ">

              <div className="
                prose
                prose-lg
                max-w-none
                prose-img:rounded-2xl
                prose-headings:font-bold
                prose-p:text-zinc-700
              ">

                <ReactMarkdown>
                  {article}
                </ReactMarkdown>

              </div>
            </div>


            {/* GENERATED VISUALS */}

            {generateImages &&
              images.length > 0 && (

              <div className="mt-16">

                <div className="
                  flex
                  items-center
                  gap-3
                  mb-8
                ">

                  <ImageIcon size={24} />

                  <h2 className="
                    text-3xl
                    font-bold
                  ">
                    Generated Visuals
                  </h2>
                </div>


                <div className="
                  grid
                  lg:grid-cols-2
                  gap-8
                ">

                  {images.map((img, index) => (

                    <div
                      key={index}
                      className="
                        bg-white
                        rounded-[30px]
                        overflow-hidden
                        shadow-lg
                      "
                    >

                      <img
                        src={`
http://127.0.0.1:8000${img.image_path}
`}
                        alt="generated"
                        className="
                          w-full
                          h-[320px]
                          object-cover
                        "
                      />
                      

                      <div className="p-6">

                        <h3 className="
                          font-semibold
                          text-lg
                        ">
                          {img.caption}
                        </h3>

                        <p className="
                          text-zinc-500
                          mt-2
                        ">
                          {img.image_type}
                        </p>

                      </div>
                    </div>
                  ))}

                </div>
              </div>
            )}

          </div>
        )}

      </div>

    </div>
  )
}