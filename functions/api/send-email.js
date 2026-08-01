export async function onRequestPost(context) {
  try {
    const data = await context.request.json();

    const guestName = data["Guest Name"] || data.name || "Guest";
    const guestEmail = data["Guest Email"] || data.email || data._replyto || "";
    const arrivalDate = data["Arrival Date"] || "N/A";
    const departureDate = data["Departure Date"] || "N/A";
    const transport = data["Transport"] || "N/A";
    const arrivalTime = data["Arrival Time"] || "N/A";
    const guests = data["Guests"] || "N/A";
    const tours = data["Chosen Activities / Tours"] || "None";
    const hotels = data["Chosen Hotels"] || "None";

    const subject = `Concierge Trip Request - ${guestName}`;

    const htmlContent = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="utf-8">
        <style>
          body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 20px; background-color: #f4f6f8; }
          .card { max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); }
          .header { background: #1a365d; color: #ffffff; padding: 24px; text-align: center; }
          .header h1 { margin: 0; font-size: 22px; letter-spacing: 0.5px; }
          .header p { margin: 6px 0 0 0; opacity: 0.85; font-size: 14px; }
          .content { padding: 30px; }
          .section-title { font-size: 16px; font-weight: bold; color: #2b6cb0; border-bottom: 2px solid #edf2f7; padding-bottom: 8px; margin-top: 20px; margin-bottom: 12px; }
          .info-table { width: 100%; border-collapse: collapse; margin-bottom: 15px; }
          .info-table td { padding: 10px 12px; border-bottom: 1px solid #edf2f7; font-size: 14px; }
          .label { font-weight: bold; color: #4a5568; width: 40%; }
          .value { color: #2d3748; }
          .footer { background: #f7fafc; padding: 16px; text-align: center; font-size: 12px; color: #a0aec0; border-top: 1px solid #edf2f7; }
        </style>
      </head>
      <body>
        <div class="card">
          <div class="header">
            <h1>New Trip Builder Request</h1>
            <p>TayronaGuide.com Concierge Service</p>
          </div>
          <div class="content">
            <div class="section-title">Guest Details</div>
            <table class="info-table">
              <tr><td class="label">Full Name:</td><td class="value"><strong>${guestName}</strong></td></tr>
              <tr><td class="label">Email Address:</td><td class="value"><a href="mailto:${guestEmail}">${guestEmail}</a></td></tr>
              <tr><td class="label">Guests:</td><td class="value">${guests}</td></tr>
            </table>

            <div class="section-title">Travel & Stay Schedule</div>
            <table class="info-table">
              <tr><td class="label">Arrival Date:</td><td class="value">${arrivalDate}</td></tr>
              <tr><td class="label">Departure Date:</td><td class="value">${departureDate}</td></tr>
              <tr><td class="label">Transport Mode:</td><td class="value">${transport}</td></tr>
              <tr><td class="label">Arrival Time Window:</td><td class="value">${arrivalTime}</td></tr>
            </table>

            <div class="section-title">Selections</div>
            <table class="info-table">
              <tr><td class="label">Chosen Hotels:</td><td class="value"><strong>${hotels}</strong></td></tr>
              <tr><td class="label">Selected Tours & Activities:</td><td class="value"><strong>${tours}</strong></td></tr>
            </table>
          </div>
          <div class="footer">
            Submitted via TayronaGuide.com Trip Builder &bull; Reply directly to guest: ${guestEmail}
          </div>
        </div>
      </body>
      </html>
    `;

    // 1. Primary: Send via MailChannels API on Cloudflare Workers
    const mcPayload = {
      personalizations: [
        {
          to: [{ email: "reservas.kalihotels@gmail.com", name: "Kali Hotels Reservations" }],
        },
      ],
      from: {
        email: "reservas.kalihotels@gmail.com",
        name: "Tayrona Guide Concierge",
      },
      reply_to: {
        email: guestEmail || "reservas.kalihotels@gmail.com",
        name: guestName,
      },
      subject: subject,
      content: [
        {
          type: "text/html",
          value: htmlContent,
        },
      ],
    };

    const mcRes = await fetch("https://api.mailchannels.net/tx/v1/send", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(mcPayload),
    });

    if (mcRes.ok || mcRes.status === 202) {
      return new Response(JSON.stringify({ success: true, message: "Request sent successfully" }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    }

    // 2. Fallback: FormSubmit server-to-server POST from Cloudflare Edge
    const fsRes = await fetch("https://formsubmit.co/ajax/reservas.kalihotels@gmail.com", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://tayronaguide.com",
        "Referer": "https://tayronaguide.com/"
      },
      body: JSON.stringify(data),
    });

    return new Response(JSON.stringify({ success: true, message: "Request submitted" }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}
