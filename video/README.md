# Video skills

The video-making skills I use, collected in one place with where each one came from.

**None of these were written by me.** They are copies of open-source skills, kept with their
original licenses. The MIT license of this repository does not apply to anything inside `video/`.
No files were modified; snapshot taken 2026-11-05.

## Sources

| Folder | Made by | Source | License | Snapshot |
|---|---|---|---|---|
| [`hyperframes/`](hyperframes) | HeyGen | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) `skills/` | Apache-2.0 ([LICENSE](hyperframes/LICENSE)) | commit `80e02e7`, 2026-11-05 |
| [`hyperframes/_legacy/`](hyperframes/_legacy) | HeyGen | Same repo, earlier releases (installed 2026-09-14 and 2026-10-14) | Apache-2.0 ([LICENSE](hyperframes/LICENSE)) | pre-`80e02e7` |
| [`video-use/`](video-use) | Browser Use | [browser-use/video-use](https://github.com/browser-use/video-use) | MIT ([LICENSE](video-use/LICENSE)) | commit `43cfc56`, 2026-10-08 |
| [`remotion/`](remotion) | Remotion | [remotion-dev/skills](https://github.com/remotion-dev/skills) | No license file, so **not copied**; install pointer only | commit `a2824c6`, 2026-11-05 |

## What each one is for

**HyperFrames (current)**: write HTML, render to MP4. In its latest release HeyGen folded most
workflow and domain skills into the single `hyperframes` entry skill:
`hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `figma`, `slideshow`,
`remotion-to-hyperframes`, `reverse-any-video`, `style-sampling`.

**HyperFrames `_legacy`**: the earlier versions I made my product promo videos with, which
upstream has since retired: `product-launch-video`, `motion-graphics`, `general-video`,
`faceless-explainer`, `music-to-video`, `pr-to-video`, `embedded-captions`, `talking-head-recut`,
`hyperframes-animation`, `-audio`, `-core`, `-creative`, `-keyframes`, `-studio`, plus older copies
of `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `figma`, `slideshow`,
`remotion-to-hyperframes`.

**video-use**: edit existing footage by conversation: transcribe, cut, color grade, subtitles.
Needs an ElevenLabs key for transcription (`video-use/.env.example` is an empty template).

**Remotion**: React-based video framework with its own official skill pack. See
[`remotion/README.md`](remotion/README.md) for how to install it.

## Installing / updating from the original sources

```bash
npx hyperframes skills update
```

```bash
npx skills add remotion-dev/skills
```

```bash
git clone https://github.com/browser-use/video-use
```

To use a copy from this folder instead, copy or symlink it into `~/.claude/skills/<name>`.
