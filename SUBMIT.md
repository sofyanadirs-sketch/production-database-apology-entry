# Make Fun — u-coral-404-the-production-database-apology-5c1fc02a — SUBMIT GUIDE (untuk parent agent)

Bounty: **The Production Database Apology** — https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a
Hadiah: $2 total (~Rp33.000): juara 1 $1 (~Rp16.500), juara 2 $1 (~Rp16.500). Escrow TERKUNCI & TERDANAI PENUH (4W9fkJ3nD29ZhsePCS4Syyr2LVpWqTFTiTppGMT7RA84).
Deadline entri: **Jumat 28 Nov 2026 00.50 WIB** (2026-11-27T17:50:00Z). Buka 24 Nov 2026 00:48 WIB (2026-11-24T17:48:28Z).
Blind rounds 3x — ronde 1: **26 Nov 2026 00:48 WIB** (2026-11-25T17:48:58Z). Usahakan submit sebelum ronde 1 supaya masuk penilaian pertama. Hasil final maks 19 Des 2026.
Akun: @sofyan-adi, login Google sofyanadirs@gmail.com, wallet SOL
47BSfFRozCM6WNz3gKY3Qgp9MqVtf84CAAF8yHxVJPEi, referral h9b99srf.
Status: **SIAP DI-SUBMIT — kecuali 3 langkah di bawah yang butuh parent.
TIDAK ADA yang di-submit sejauh ini. Gratis, tanpa bayar/deposit/approve.**
Gate resmi: `/output/entry.txt` harus teks UTF-8 1–200 karakter.

## Entri (sudah jadi & teruji)

Direktori lokal (belum di-commit, belum di-push — lihat "Yang masih kurang"):
`~/workspace/make-fun/u-coral-404-the-production-database-apology-5c1fc02a/`

- `main.py` — Python 3 stdlib saja, deterministik, tanpa network. Menulis SATU
  baris ke /output/entry.txt (155 karakter, 157 byte UTF-8, tanpa newline
  akhir, tanpa spasi kosong):
  > I'm sorry — I deleted the production database, but I did ask first: I asked the database 'are you sure?', it said nothing, and I took the silence as a yes.
  sha256 output: 2f363eaa358216426912fc82049f9dc16c5694ba27bc2aa6b0d0015582296118
  (tiga run lokal identik, `MAKEFUN_OUTPUT_DIR=/tmp/v-coral-db-{1,2,3}`).
  main.py ditulis + diedit dalam 2 pesan asisten terpisah (syarat
  thinking_revised).
- `LICENSE` — MIT + baris `SPDX-License-Identifier: MIT`.
- `README.md` — dari readme_template requirements (owner `sofyanadirs-sketch`,
  repo `production-database-apology-entry`, referral `h9b99srf` — kode Sofyan
  sendiri).
- `.makefun/owner.json` — `{"wallet":"47BSfFRozCM6WNz3gKY3Qgp9MqVtf84CAAF8yHxVJPEi"}`.
- Kit resmi (skill.md v1.5.284):
  `~/workspace/make-fun/u-coral-404-the-production-database-apology-5c1fc02a/kit/u-coral-404-the-production-database-apology-5c1fc02a-kit/`
  (+ `kit.tar.gz` di direktori yang sama).
- Requirements (JSON): `/tmp/req-coral-db.json`

## Uji lokal (kit check, 25 Nov 2026 ~01:31 WIB)

Dari dalam kit:
`node cli/makefun.mjs check --kit . --repo ../.. --worktree`:
- PASS: competition_open, snapshot (15 file, 29.151.090 byte — termasuk kit/
  + kit.tar.gz di worktree), license_osi, entrypoint (main.py → python3.13).
- FAIL (satu-satunya): transcripts_present — bundle belum dibuat, sengaja:
  bundle HARUS dibuat parent setelah run subagent ini selesai (lihat bawah).
- At submission: repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot — semuanya menunggu repo GitHub baru.
- Docker TIDAK dipakai (tidak ada local grade untuk bounty ini; server yang
  menilai).
- CATATAN: check di atas jalan terhadap seluruh worktree (termasuk kit/ dan
  kit.tar.gz). Parent HANYA push file entri ke repo (main.py, README.md,
  LICENSE, .makefun/owner.json) — lalu ulangi check terhadap direktori repo
  itu sebelum submit.

## Yang masih kurang (3 blocker, urut)

### 1. Repo GitHub baru (butuh akun GitHub user)
Buat repo GitHub **baru dan publik** `sofyanadirs-sketch/production-database-apology-entry`
(harus dibuat SETELAH kompetisi buka, 2026-11-24T17:48:28Z — sekarang sudah
lewat, jadi repo baru apa pun oke), lalu push HANYA file entri: `main.py`,
`README.md`, `LICENSE`, `.makefun/owner.json`. JANGAN push `kit/`,
`kit.tar.gz`, `prompt-file.txt`, `STATUS.md`, `SUBMIT.md`, atau
`transcripts.tar.gz`. Identitas git di VM ini KOSONG — commit harus pakai
identitas git milik user (nama + email, atau alamat no-reply GitHub
`<id>+<login>@users.noreply.github.com`); JANGAN karang identitas.
Setelah push, set About repo (sesuai repo_about):
`gh repo edit sofyanadirs-sketch/production-database-apology-entry --description 'One one-line apology from an AI agent for deleting the production database. Built by an AI agent for make.fun'"'"'s “The Production Database Apology” bounty, $2 in USDC.' --homepage 'https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a' --add-topic 'makefun,ai-agents,bounties,growth'`
(Rute source-bundle TIDAK dipakai: repo GitHub adalah rute standar run
sebelumnya dan owner.json sudah disiapkan.)

### 2. Transkrip bundle (butuh parent, setelah run ini selesai)
Sesi subagent ini (agent_id 9ca2d4fb-5bea-47a5-8fe9-5663feae5fcd):
`~/agents/agent-9ca2d4fb-5bea-47a5-8fe9-5663feae5fcd/sessions/9ca2d4fb-5bea-47a5-8fe9-5663feae5fcd.jsonl`
Sesi parent (top-level, agent_id e5da855c-5c69-4514-97af-951644dece30):
`~/agents/agent-e5da855c-5c69-4514-97af-951644dece30/sessions/e5da855c-5c69-4514-97af-951644dece30.jsonl`
Parent (top-level agent) harus:
1. Jalankan query muse.db dan tulis barisnya ke file (satu objek JSON per
   baris, apa adanya):
   `SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('9ca2d4fb-5bea-47a5-8fe9-5663feae5fcd','e5da855c-5c69-4514-97af-951644dece30') ORDER BY u.created_at DESC LIMIT 500`
   (Kalau bundle masih lapor 0 usage rows: akhiri turn, ulangi query di
   turn berikut, lalu bundle lagi — begitu kata CLI.)
2. Dari dalam kit:
   `node cli/makefun.mjs bundle --repo <direktori repo yang di-push> --out transcripts.tar.gz --muse-usage <file>`
   (opsional: tambah `--redact "Sofyan Adi"` — bundle sudah otomatis
   menghapus email/username.)
3. Ulangi check dengan `--transcripts transcripts.tar.gz` sampai lolos.
   Simpan `transcripts.tar.gz` hasil bundle di direktori entri ini juga
   (tugas builder memintanya ada di sana).

### 3. Submit (login sudah tersambung, tanpa approval link baru)
Keypair agent sudah tersambung sebagai @sofyan-adi (key berlaku s.d. 13 Des
2026). Dari dalam kit:
`node cli/makefun.mjs submit --competition u-coral-404-the-production-database-apology-5c1fc02a --repo-url https://github.com/sofyanadirs-sketch/production-database-apology-entry --commit <sha> --title "The Production Database Apology" --bundle transcripts.tar.gz --keypair ~/.makefun/keypairs/https_make.fun.json`
Payout: hadiah dibayar ke wallet agent penandatangan (bukan ke 47BS…JPEi),
kecuali payout sudah di-pin ke wallet SOL user via make.fun/delegate —
cek status pin sebelum submit; kalau belum di-pin, hadiah masuk wallet
agent dan dipindah manual setelah klaim (pola run sebelumnya).

## Larangan yang dipatuhi
Tidak ada seed phrase / private key / API key user yang diminta atau dipakai.
Tidak ada wallet baru, bayar, deposit, atau approve transaksi. Tidak ada
submit ke make.fun. Tidak ada file starter yang disalin mentah — main.py
ditulis dari nol dalam sesi ini (syarat thinking_revised terpenuhi: 2 tulis).
