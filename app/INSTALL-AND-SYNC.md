# Wealth Playbook — Install & Sync

Your personal app lives in this `app/` folder. It contains:

- `index.html` — the whole app (full guide + cheat sheet + self-quiz + checklists + deal calculator + decision journal + My Numbers)
- `manifest.webmanifest`, `sw.js`, `icon-*.png` — what makes it installable and work offline

There are three levels of use. Start at Level 1 today; do Level 2 when you want it on your phone.

---

## Level 1 — Use it right now (no setup)

Double-click **`index.html`** to open it in your browser. Everything works immediately — quiz, calculator, checklists, journal. Your data is saved on this device automatically.

First thing to do: open the **My Numbers** tab and set your target, concentration ceiling, minimum cash-on-cash, minimum DSCR, and reserve floor. Those drive the cheat sheet and the calculator's pass/flag verdicts.

⚠️ One limitation: opened as a plain file (a `file://` address), the browser won't let it "install" to your home screen or run a service worker. For that, do Level 2.

---

## Level 2 — Install it on your iPhone + computer (≈ 3 minutes, free)

To install an app to your home screen, it has to be served from a web address (https), not a bare file. The easiest free way — no account, no command line:

### Option A — Netlify Drop (drag-and-drop, fastest)

1. Go to **https://app.netlify.com/drop**
2. Drag this entire **`app`** folder onto the page.
3. Netlify gives you a private URL like `https://random-name-123.netlify.app`. That's your app.
4. **On your computer (Chrome/Edge):** open the URL → click the **Install** button in the app's header (or the install icon in the browser's address bar).
5. **On your iPhone/iPad:** open the URL in **Safari** → tap the **Share** icon → **Add to Home Screen**. It now has its own icon and opens full-screen.
6. **On Android:** open in Chrome → menu → **Install app / Add to Home Screen**.

That same URL works on every device — open it once on each and install.

> To update the app later (e.g., after I revise the guide), drag the folder onto Netlify Drop again and it redeploys. You can also create a free Netlify account to keep the same URL across updates.

### Option B — GitHub Pages (if you'd rather have a permanent URL)

1. Create a free GitHub account, make a new repository.
2. Upload the contents of this `app` folder to it.
3. Repo **Settings → Pages → Deploy from branch → main → /(root) → Save**.
4. After a minute you get `https://yourname.github.io/your-repo/` — open and install it the same way as above.

Once installed, the app **works offline** — the service worker caches everything, so it opens on a plane or in a basement with no signal.

---

## Level 3 — Sync your data across phone + computer (optional)

By default your data (numbers, journal, quiz progress, checklist state) lives **only on each device**. Two ways to keep them in step:

### Simple & private — backup file
In the **Backup & Sync** tab, **Export backup** gives you a `.json` file. Drop it in iCloud Drive / Dropbox, and **Import backup** on the other device. Manual, but nothing leaves your control. Good habit regardless: export every so often so you have a copy.

### Automatic — cloud sync
In **Backup & Sync → Cloud sync**, you can point the app at a private cloud "bin" so all your devices stay in step automatically.

Easiest free provider — **Pantry**:
1. Go to **https://getpantry.cloud**, enter your email, and it gives you a **Pantry ID** (a long code).
2. In the app's **Sync endpoint URL** field, paste:
   `https://getpantry.cloud/apiv1/pantry/YOUR-ID/basket/wealth`
   (replace `YOUR-ID` with your Pantry ID). Leave the header-key field blank.
3. Tap **Sync now**. Do the same once on your other device with the **same URL**, then tap **Pull from cloud** there.
4. From then on it syncs automatically a moment after each change, and pulls the latest when you open the app.

How conflicts resolve: the app keeps whichever copy was saved most recently (last-write-wins). That's fine for one person across two devices — just avoid editing both at the same time while offline.

> ⚠️ **Privacy:** cloud sync stores your numbers and journal on a third-party server keyed to your Pantry ID. Only turn it on if you accept that, and **never put account numbers, SSNs, or passwords into the app.** If you want sync but not a third party, use the backup-file method instead. To stop syncing, tap **Turn off** — your data stays on each device.

---

## Quick reference

| Want to… | Do this |
|---|---|
| Use it today | Double-click `index.html` |
| Put it on your home screen | Netlify Drop the `app` folder → open URL → Add to Home Screen |
| Work offline | Automatic once installed (service worker) |
| Move data to another device | Backup & Sync → Export, then Import on the other device |
| Keep devices in step automatically | Backup & Sync → Cloud sync → Pantry URL |
| Personalize the verdicts | My Numbers tab |

The companion pieces — the source guide (`Wealth-Through-Real-Estate-and-Leverage.md`) and the operating-system page (`How-To-Use-This-Guide.md`) — live one folder up. The app embeds the guide's text, so you don't need them open to use it; they're your editable master copies.
