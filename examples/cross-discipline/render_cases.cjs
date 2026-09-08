const fs=require('fs'),path=require('path');
let sharp;try{sharp=require('sharp')}catch(e){if(!process.env.FIGURE_NODE_MODULES)throw e;sharp=require(path.join(process.env.FIGURE_NODE_MODULES,'sharp'))}
const cases=['chemistry-sn2','earth-confined-aquifer','ecology-carbon','research-causal-dags'];
Promise.all(cases.map(async name=>{const dir=path.join(__dirname,name);const info=await sharp(fs.readFileSync(path.join(dir,'figure.svg')),{density:144}).png().toFile(path.join(dir,'figure.png'));console.log(name,JSON.stringify(info))})).catch(e=>{console.error(e);process.exitCode=1});
