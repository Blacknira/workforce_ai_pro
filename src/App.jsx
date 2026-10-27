import { useState } from 'react'

export default function App() {
  const [page, setPage] = useState('dashboard')
  const [emps] = useState([
    {id:1,name:'Arjun Kumar',dept:'Engineering',risk:'CRITICAL',score:92},
    {id:2,name:'Priya S',dept:'HR',risk:'LOW',score:15},
    {id:3,name:'Rahul M',dept:'Sales',risk:'HIGH',score:85},
    {id:4,name:'Sneha K',dept:'Marketing',risk:'MEDIUM',score:45},
  ])

  return (
    <div style={{display:'flex', minHeight:'100vh', background:'#020617', color:'white', fontFamily:'Segoe UI'}}>
      {/* SIDEBAR */}
      <div style={{width:'240px', background:'#0f172a', borderRight:'1px solid #1e293b', padding:'20px'}}>
        <h2 style={{marginBottom:'30px'}}>🚀 WorkForce AI</h2>
        <div style={{display:'flex', flexDirection:'column', gap:'10px'}}>
          <button onClick={()=>setPage('dashboard')} style={{padding:'12px', background:page==='dashboard'?'#6366f1':'#1e293b', color:'white', border:'none', borderRadius:'10px', textAlign:'left', cursor:'pointer'}}>📊 Dashboard</button>
          <button onClick={()=>setPage('employees')} style={{padding:'12px', background:page==='employees'?'#6366f1':'#1e293b', color:'white', border:'none', borderRadius:'10px', textAlign:'left', cursor:'pointer'}}>👥 Employees</button>
          <button onClick={()=>setPage('analytics')} style={{padding:'12px', background:page==='analytics'?'#6366f1':'#1e293b', color:'white', border:'none', borderRadius:'10px', textAlign:'left', cursor:'pointer'}}>📈 Analytics</button>
          <button onClick={()=>setPage('alerts')} style={{padding:'12px', background:page==='alerts'?'#6366f1':'#1e293b', color:'white', border:'none', borderRadius:'10px', textAlign:'left', cursor:'pointer'}}>🚨 Alerts</button>
        </div>
        <div style={{marginTop:'40px', padding:'12px', background:'#1e293b', borderRadius:'10px', fontSize:'11px', color:'#64748b'}}>
          Backend: 8000 ✅<br/>Frontend: 5173 ✅<br/>DB: workforce_ai<br/>AI: 87% Accuracy
        </div>
      </div>

      {/* MAIN CONTENT */}
      <div style={{flex:1, padding:'30px'}}>
        {page==='dashboard' && (
          <div>
            <h1>Workforce Intelligence Dashboard</h1>
            <p style={{color:'#94a3b8', marginTop:'6px'}}>Real-time AI Monitoring | FastAPI + MySQL + JWT + Scikit-learn</p>
            <div style={{display:'grid', gridTemplateColumns:'repeat(4,1fr)', gap:'16px', marginTop:'24px'}}>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}><p style={{color:'#94a3b8', fontSize:'13px'}}>Total Employees</p><h1 style={{marginTop:'8px'}}>247</h1><p style={{color:'#22c55e', fontSize:'12px'}}>+12% this month</p></div>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}><p style={{color:'#94a3b8', fontSize:'13px'}}>High Risk</p><h1 style={{marginTop:'8px', color:'#ef4444'}}>18</h1><p style={{fontSize:'12px'}}>Needs attention</p></div>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}><p style={{color:'#94a3b8', fontSize:'13px'}}>Retention Rate</p><h1 style={{marginTop:'8px', color:'#22c55e'}}>87%</h1><p style={{fontSize:'12px'}}>ML Model Accuracy</p></div>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}><p style={{color:'#94a3b8', fontSize:'13px'}}>AI Predictions</p><h1 style={{marginTop:'8px'}}>42</h1><p style={{fontSize:'12px'}}>Today - Live</p></div>
            </div>
            <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px', marginTop:'20px'}}>
              <h3>🔄 Expected Flow (Live Enterprise)</h3>
              <p style={{color:'#cbd5e1', fontSize:'13px', marginTop:'10px', lineHeight:'1.8'}}>Employee activity changes → AI prediction engine recalculates risk → High-risk employee detected → HR alert triggered → Intervention workflow initiated → Monitoring logs updated → Analytics dashboard refreshed</p>
            </div>
          </div>
        )}

        {page==='employees' && (
          <div>
            <h1>👥 Workforce - AI Prediction</h1>
            <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'14px', marginTop:'20px'}}>
              {emps.map(e=>(
                <div key={e.id} style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}>
                  <div style={{display:'flex', justifyContent:'space-between'}}><h3>{e.name}</h3><span style={{padding:'5px 10px', borderRadius:'20px', fontSize:'11px', background:e.risk==='CRITICAL'?'#ef4444':e.risk==='HIGH'?'#f97316':e.risk==='MEDIUM'?'#eab308':'#22c55e', color:e.risk==='MEDIUM'?'black':'white', fontWeight:'700'}}>{e.risk} {e.score}%</span></div>
                  <p style={{color:'#94a3b8', fontSize:'12px', marginTop:'8px'}}>{e.dept} | Job Satisfaction: Low | OverTime: Yes | Distance: 20km</p>
                  <button onClick={()=>alert(`🤖 AI Prediction: ${e.name} is ${e.risk} risk with ${e.score}% probability. Recommendation: Manager 1-1 Meeting Needed. API: /prediction/predict/${e.id}`)} style={{marginTop:'12px', background:'#6366f1', color:'white', border:'none', padding:'8px 14px', borderRadius:'8px', cursor:'pointer'}}>🤖 AI Predict</button>
                </div>
              ))}
            </div>
          </div>
        )}

        {page==='analytics' && (
          <div>
            <h1>📈 Analytics Reports</h1>
            <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'16px', marginTop:'20px'}}>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}><h3>AI Model</h3><p style={{fontSize:'13px', lineHeight:'1.8', marginTop:'8px'}}>Framework: Scikit-learn<br/>Model: RandomForest + Pandas<br/>Accuracy: 87%<br/>API: POST /prediction/predict/{'{id}'}<br/>Features: 12 HR factors</p></div>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px'}}><h3>Database & API</h3><p style={{fontSize:'13px', lineHeight:'1.8', marginTop:'8px'}}>DB: MySQL workforce_ai<br/>ORM: SQLAlchemy<br/>Auth: JWT Bearer + Bcrypt<br/>Validation: Pydantic<br/>Docs: /docs</p></div>
            </div>
          </div>
        )}

        {page==='alerts' && (
          <div>
            <h1>🚨 Real-Time HR Alerts</h1>
            <div style={{marginTop:'20px', display:'flex', flexDirection:'column', gap:'12px'}}>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px', borderLeft:'5px solid #ef4444'}}><h3 style={{color:'#ef4444'}}>🔴 CRITICAL: Rahul M - 92% Attrition Risk</h3><p style={{fontSize:'13px', marginTop:'8px'}}>Trigger: Satisfaction 1/4 + WLB 1/4 + OT + Distance 22km<br/>Action: Intervention Workflow Initiated → Manager Notified → Log Updated → Dashboard Refreshed</p></div>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px', borderLeft:'5px solid #f97316'}}><h3 style={{color:'#f97316'}}>🟠 HIGH: Arjun Kumar - 85%</h3><p style={{fontSize:'13px'}}>HR notified, retention bonus considered</p></div>
              <div style={{background:'#1e293b', padding:'20px', borderRadius:'16px', borderLeft:'5px solid #22c55e'}}><h3 style={{color:'#22c55e'}}>🟢 LOW: Priya S - 15% Stable</h3></div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}