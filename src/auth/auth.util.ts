// const fs = require("fs");

function enforcePolicy(subject, object, action, context) {
    // const policy = JSON.parse(fs.readFileSync("policy.json", "utf-8"));

    // for (let i = 0; i < policy.rules.length; i++) {
    //     let rule = policy.rules[i];
    //     if (rule.subject.role === subject.role &&
    //         rule.object.type === object.type &&
    //         rule.action === action) {
    //         if (rule.condition) {
    //             if (rule.condition.ip) {
    //                 let ipRange = rule.condition.ip;
    //                  if (!checkIp(context.ip, ipRange)) {
    //                      continue;
    //                  }
    //             }
    //         }
    //         return rule.effect === "permit";
    //     }
    // }

    return false;
}

function checkIp(ip, range) {
    // check if the given IP falls within the range
}
